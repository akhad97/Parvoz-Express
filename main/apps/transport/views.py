from django.db.models import Q, Sum
from django.utils import timezone
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count

from .models import Transport, TransportCalculation
from .serializers import (
    TransportSerializer, 
    TransportCreateSerializer, 
    TransportCalculationSerializer, 
    TransportCalculationCreateSerializer
)
from ..common.views import CustomListView, CustomCreateAPIView, CustomDetailView
from ..common.utils import get_prepayment_percentage, get_remained_amount_percentage, get_unpaid_percentage
from ..common.validations import CustomValidationError



class TransportListAPIView(CustomListView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer

    def get_queryset(self):
        params = self.request.query_params
        query = params.get('query', None)

        expenses = Transport.objects.all() # need to filter based on user or smth 

        if query:
            expenses = expenses.filter(Q(transport_type__icontains=query) | Q(city__icontains=query) | Q(full_name__icontains=query))

        return expenses

transport_list_api_view = TransportListAPIView.as_view()


class TransportCreateAPIView(CustomCreateAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportCreateSerializer

transport_create_api_view = TransportCreateAPIView.as_view()


class TransportDetailAPIView(CustomDetailView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    lookup_field = 'guid'

transport_detail_api_view = TransportDetailAPIView.as_view()


@api_view(['GET'])
def transport_type_percentage(request):
    total_count = Transport.objects.count()
    counts = Transport.objects.values('transport_type').annotate(count=Count('transport_type'))
    percentages = {}
    for item in counts:
        transport_type = item['transport_type']
        count = item['count']
        percentage = count / total_count * 100
        percentages[transport_type] = round(percentage, 2)

    data = []
    for transport_type, percentage in percentages.items():
        data.append({
            'transport_type': transport_type,
            'percentage': percentage
        })

    return Response(data)

transport_type_percentage_api_view = transport_type_percentage


class TransportCalculationListAPIView(CustomListView):
    queryset = TransportCalculation.objects.all()
    serializer_class = TransportCalculationSerializer

transportcalculation_list_api_view = TransportCalculationListAPIView.as_view()


class SingleTransportCalculationDetailAPIView(CustomListView):
    queryset = TransportCalculation.objects.all()
    serializer_class = TransportCalculationSerializer

    def get_queryset(self):
        params = self.request.query_params

        qs = TransportCalculation.objects.filter(transport=self.kwargs['pk'])
                
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

single_transport_calculation_detail_api_view = SingleTransportCalculationDetailAPIView.as_view()


class TransportCalculationCreateAPIView(CustomCreateAPIView):
    queryset = TransportCalculation.objects.all()
    serializer_class = TransportCalculationCreateSerializer
    
transportcalculation_create_api_view = TransportCalculationCreateAPIView.as_view()


@api_view(['GET'])
def transport_calculation_analytics(self):
    model = TransportCalculation
    prepayment_percentage = get_prepayment_percentage(model)
    remained_amount_percentage = get_remained_amount_percentage(model)
    unpaid_percentage = get_unpaid_percentage(model)

    data = {
        **prepayment_percentage,
        **remained_amount_percentage,
        'unpaid_percentage': unpaid_percentage,
    }
    return Response(data)