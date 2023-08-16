from django.db.models import Q, Sum
from django.utils import timezone
from datetime import datetime
from rest_framework import generics
from rest_framework.response import Response
from .models import (
    Visa, 
    VisaCalculation,
    VisaBook
) 
from ..common.views import CustomListView, CustomDetailView
from ..common.validations import CustomValidationError
from .serializers import (
    VisaSerializer,
    VisaCreateSerializer,
    VisaCalculationSerializer,
    VisaCalculationCreateSerializer,
    VisaBookCreateSerializer,
    VisaBookListSerializer
)


class VisaListAPIView(CustomListView):
    queryset = Visa.objects.all()
    serializer_class = VisaSerializer

visa_list_api_view = VisaListAPIView.as_view()


class VisaDetailAPIVIew(CustomDetailView):
    queryset = Visa.objects.all()
    serializer_class = VisaCreateSerializer

visa_detail_api_view = VisaDetailAPIVIew.as_view()


class VisaCreateAPIView(generics.CreateAPIView):
    queryset = Visa.objects.all()
    serializer_class = VisaCreateSerializer

visa_create_api_view = VisaCreateAPIView.as_view()


class VisaCalculationListAPIView(CustomListView):
    queryset = VisaCalculation.objects.all()
    serializer_class = VisaCalculationSerializer

visacalculation_list_api_view = VisaCalculationListAPIView.as_view()


class VisaCalculationCreateAPIView(generics.CreateAPIView):
    queryset = VisaCalculation.objects.all()
    serializer_class = VisaCalculationCreateSerializer

visacalculation_create_api_view = VisaCalculationCreateAPIView.as_view()


class SingleVisaCalculationDetailAPIView(CustomListView):
    queryset = VisaCalculation.objects.all()
    serializer_class = VisaCalculationSerializer

    def get_queryset(self):
        params = self.request.query_params

        qs = VisaCalculation.objects.filter(visa=self.kwargs['pk'])
                
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

single_visa_calculation_detail_api_view = SingleVisaCalculationDetailAPIView.as_view()


class VisaBookCreateAPIView(generics.CreateAPIView):
    queryset = VisaBook.objects.all()
    serializer_class = VisaBookCreateSerializer

visabook_create_api_view = VisaBookCreateAPIView.as_view()


class VisaBookListAPIView(CustomListView):
    queryset = VisaBook.objects.all()
    serializer_class = VisaBookListSerializer

visabook_list_api_view = VisaBookListAPIView.as_view()


class VisaBookUpdateAPIView(generics.UpdateAPIView):
    queryset = VisaBook.objects.all()
    serializer_class = VisaBookCreateSerializer
    lookup_field = 'guid'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serilizer(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Successfully updated'})
        return Response({'message': 'failed', 'details': serializer.errors})

visa_book_update_api_view = VisaBookUpdateAPIView.as_view()