from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Q, Sum
from django.utils import timezone
from datetime import datetime

from .models import (
    Hotel, 
    HotelCalculation,
    HotelBook
)
from .serializers import(
    HotelListSerializer,
    HotelCreateSerializer,
    HotelCalculationListSerializer,
    HotelCalculationCreateSerializer,
    HotelBookCreateSerializer,
    HotelBookListSerializer,
    HotelBookUpdateSerializer
) 
from ..common.views import CustomListView, CustomCreateAPIView, CustomDetailView
from ..common.utils import get_prepayment_percentage, get_remained_amount_percentage, get_unpaid_percentage
from ..common.validations import CustomValidationError



class HotelLandingSeachAPIView(CustomListView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer

    def get_queryset(self):
        params = self.request.query_params
        city = params.get('city', None)
        hotel_ranks = self.request.GET.get('hotel_ranks', None)
        nutritions = params.get('nutritions', None)
        start_price = params.get('start_price', None)
        end_price = params.get('end_price', None)

        qs = Hotel.objects.all()

        if city:
            qs = qs.filter(city__icontains=city)
        
        if hotel_ranks:
            qs = qs.filter(number_of_stars__in=[rank for rank in hotel_ranks.split(',')])

        if nutritions:
            qs = qs.filter(nutrition__in=[nutrition for nutrition in nutritions.split(',')])

        if start_price and end_price:
            query = Q(single_room_price__range=(start_price, end_price)) | \
                Q(double_room_price__range=(start_price, end_price)) | \
                Q(triple_room_price__range=(start_price, end_price)) | \
                Q(quadruple_room_price__range=(start_price, end_price))
            qs = qs.filter(query)
        
        return qs

hotel_landing_serach_api_view = HotelLandingSeachAPIView.as_view()


class HotelListAPIView(CustomListView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer

    def get_queryset(self):
        params = self.request.query_params
        title = params.get('title', None)
        hotel_rank = params.get('hotel_rank')

        qs = Hotel.objects.all() 

        if title:
            qs = qs.filter(title__icontains=title)

        if hotel_rank:
            qs = qs.filter(number_of_stars__iexact=hotel_rank)

        return qs

hotel_list_api_view = HotelListAPIView.as_view()


class HotelCreateAPIView(CustomCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.object = serializer.save()
        self.object.data = request.data['data']
        self.object.save()

        return self.success_response(serializer.data)

hotel_create_api_view = HotelCreateAPIView.as_view()


class HotelDetailAPIView(CustomDetailView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    lookup_field = 'guid'

hotel_detail_api_view = HotelDetailAPIView.as_view()


class HotelCalculationListAPIView(CustomListView):
    queryset = HotelCalculation.objects.all()
    serializer_class = HotelCalculationListSerializer


    def get_queryset(self):
        params = self.request.query_params
        from_date = params.get('from_date', None)
        to_date = params.get('to_date', None)
        total_amount = params.get('total_amount', None)
        prepayment = params.get('prepayment', None)
        remained_amount = params.get('remained_amount', None)


        qs = HotelCalculation.objects.all() # need to filter based on user or smth 
        if from_date and to_date:
            try:
                from_date = datetime.strptime(params.get('from_date', None), '%Y-%m-%d')
                from_date = timezone.make_aware(from_date, timezone.get_current_timezone())
                to_date = params.get('to_date', None) + ' 23:59:59'
                to_date = datetime.strptime(to_date, '%Y-%m-%d %H:%M:%S')
                to_date = timezone.make_aware(to_date, timezone.get_current_timezone())
                qs = qs.filter(created_at__range=[from_date, to_date])
            except Exception as e:
                raise CustomValidationError(msg=e.args)

        if total_amount:
            qs = qs.filter(Q(total_amount__icontains=total_amount))
        
        if prepayment:
            qs = qs.filter(Q(prepayment__icontains=prepayment))
        
        if remained_amount:
            qs = qs.filter(Q(remained_amount__icontains=remained_amount))


        return qs

hotelcalculation_list_api_view = HotelCalculationListAPIView.as_view()


class HotelCalculationCreateAPIView(CustomCreateAPIView):
    queryset = HotelCalculation.objects.all()
    serializer_class = HotelCalculationCreateSerializer

hotelcalculation_create_api_view = HotelCalculationCreateAPIView.as_view()


class HotelCalculationDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HotelCalculation.objects.all()
    serializer_class = HotelCalculationCreateSerializer
    lookup_field='guid'

hotelcalculation_delete_api_view = HotelCalculationDeleteAPIView.as_view()


class SingleHotelCalculationDetailAPIView(CustomListView):
    queryset = HotelCalculation.objects.all()
    serializer_class = HotelCalculationListSerializer

    def get_queryset(self):
        params = self.request.query_params
        qs = HotelCalculation.objects.filter(hotel=self.kwargs['pk'])
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

single_hotel_calculation_detail_api_view = SingleHotelCalculationDetailAPIView.as_view()


@api_view(['GET'])
def hotelcalculation_analytics(request):
    model = HotelCalculation
    prepayment_percentage = get_prepayment_percentage(model)
    remained_amount_percentage = get_remained_amount_percentage(model)
    unpaid_percentage = get_unpaid_percentage(model)

    last_hotel = model.objects.select_related('hotel').last()

    data = {
        'hotel': last_hotel.hotel.title if last_hotel else None,
        **prepayment_percentage,
        **remained_amount_percentage,
        'unpaid_percentage': unpaid_percentage,
    }

    return Response(data)
 
hotelcalculation_data_api_view = hotelcalculation_analytics


class HotelBookCreateAPIView(generics.CreateAPIView):
    queryset = HotelBook.objects.all()
    serializer_class = HotelBookCreateSerializer

hotelbook_create_api_view = HotelBookCreateAPIView.as_view()


class HotelBookListAPIView(CustomListView):
    queryset = HotelBook.objects.all()
    serializer_class = HotelBookListSerializer

hotelbook_list_api_view = HotelBookListAPIView.as_view()


class HotelBookUpdateAPIView(generics.UpdateAPIView):
    queryset = HotelBook.objects.all()
    serializer_class = HotelBookUpdateSerializer
    lookup_field = 'guid'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Successfully updated'})
        return Response({'message': 'failed', 'details': serializer.errors})

hotel_book_update_api_view = HotelBookUpdateAPIView.as_view()