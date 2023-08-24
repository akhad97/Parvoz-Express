from rest_framework import generics 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from django.utils import timezone
from datetime import datetime
from ...common.validations import CustomValidationError
from ...flight.models.calculation import FlightCalculation
from ...flight.serializer.calculation import (
    FlightCalculationSerializer, 
    FlightCalculationCreateSerializer
)
from ...common.views import CustomListView, CustomCreateAPIView
from ...common.utils import (
    get_prepayment_percentage, 
    get_remained_amount_percentage, 
    get_unpaid_percentage
)



class FlightCalculationListAPIView(CustomListView):
    queryset = FlightCalculation.objects.all().select_related('flight')
    serializer_class = FlightCalculationSerializer

flightcalculation_list_api_view = FlightCalculationListAPIView.as_view()


class FlightCalculationCreateAPIView(CustomCreateAPIView):
    queryset = FlightCalculation.objects.all()
    serializer_class = FlightCalculationCreateSerializer

flightcalculation_create_api_view = FlightCalculationCreateAPIView.as_view()


@api_view(['GET'])
def flight_calculation_analytics(self):
    model = FlightCalculation
    prepayment_percentage = get_prepayment_percentage(model)
    remained_amount_percentage = get_remained_amount_percentage(model)
    unpaid_percentage = get_unpaid_percentage(model)

    data = {
        **prepayment_percentage,
        **remained_amount_percentage,
        'unpaid_percentage': unpaid_percentage,
    }
    return Response(data)

flightcalculation_analytics_api_view = flight_calculation_analytics


class SingleFlightCalculationDetailAPIView(CustomListView):
    queryset = FlightCalculation.objects.all()
    serializer_class = FlightCalculationSerializer

    def get_queryset(self):
        params = self.request.query_params
        qs = FlightCalculation.objects.filter(flight=self.kwargs['pk'])
        from_date = params.get('from_date', None)
        to_date = params.get('to_date', None)
        total_amount = params.get('total_amount', None)
        prepayment = params.get('prepayment', None)
        remained_amount = params.get('remained_amount', None)

        if from_date and to_date:
            try:
                from_date = datetime.strptime(params.get('from_date', None), '%Y-%m-%d')
                from_date = timezone.make_aware(from_date, timezone.get_current_timezone())
                to_date = params.get('to_date', None) + ' 23:59:59'
                to_date = datetime.strptime(to_date, '%Y-%m-%d %H:%M:%S')
                to_date = timezone.make_aware(to_date, timezone.get_current_timezone())
                qs = qs.filter(Q(from_date__range=[from_date, to_date]) | Q(to_date__range=[from_date, to_date]))
            except Exception as e:
                raise CustomValidationError(msg=e.args)
        if total_amount:
            qs = qs.filter(Q(total_amount__icontains=total_amount))
        if prepayment:
            qs = qs.filter(Q(prepayment__icontains=prepayment))
        if remained_amount:
            qs = qs.filter(Q(remained_amount__icontains=remained_amount))
        return qs


single_flight_calculation_detail_api_view = SingleFlightCalculationDetailAPIView.as_view()