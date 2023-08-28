from rest_framework import generics 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Q
from datetime import datetime, timezone
from ..expense.models import OtherExpense
from decimal import Decimal
from ..visa.models import Visa
from .models import (
    TourPackage, 
    TourPackageBook, 
    Contact,
    LandingData
)
from ..outfit.models import FastContact
from .serializer import (
    TourPackageSerializer,
    TourPackageCreateSerializer,
    TourPackageAnalyticsSerializer,
    TourPackageUpdateSerializer,
    TourPackageBookCreateSerializer,
    TourPackageBookListSerializer,
    ContanctSerializer,
    TourPackageBookUpdateSerializer,
    FastContanctSerializer,
    FastContactUpdateSerializer,
    LandingDataSerializer
)
from ..common.views import CustomListView, CustomCreateAPIView, CustomDetailView
from ..client.models import Client


class TourPackageListAPIVIew(CustomListView):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer

    def get_queryset(self):
        params = self.request.query_params
        title = params.get('title')
        status = params.get('status')


        qs = TourPackage.objects.filter(is_active=True)

        if title:
            qs = qs.filter(title__icontains=title)

        if status:
            qs = qs.filter(status__icontains=status)
        
        return qs

tourpackage_list_api_view = TourPackageListAPIVIew.as_view()


class TourPackageCreateAPIVIew(CustomCreateAPIView):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageCreateSerializer

tourpackage_create_api_view = TourPackageCreateAPIVIew.as_view()


class TourPackageDetailAPIVIew(generics.RetrieveAPIView):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer
    lookup_field = 'guid'

tourpackage_detail_api_view = TourPackageDetailAPIVIew.as_view()


class TourPackageUpdateAPIVIew(generics.UpdateAPIView):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageUpdateSerializer
    lookup_field = 'guid'

    def perform_update(self, serializer):
        guid = self.kwargs['guid']
        hotels = self.request.data['hotel']
        outfits = self.request.data['outfit']
        transports = self.request.data['transport']
        tourpackage = TourPackage.objects.get(guid=guid)
        tourpackage.hotel.set(hotels)
        tourpackage.outfit.set(outfits) 
        tourpackage.transport.set(transports) 
        tourpackage.save()
        serializer.save()
        return Response(serializer.data)


tourpackage_update_api_view = TourPackageUpdateAPIVIew.as_view()


class TourPackageDeleteAPIVIew(generics.DestroyAPIView):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageUpdateSerializer
    lookup_field = 'guid'

tourpackage_delete_api_view = TourPackageDeleteAPIVIew.as_view()


class TourPackageAnalyticsAPIVIew(CustomListView):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageAnalyticsSerializer

tourpackage_analytics_api_view = TourPackageAnalyticsAPIVIew.as_view()


class TourPackageLandingSearchAPIView(CustomListView):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer

    def get_queryset(self):
        params = self.request.query_params
        departure_city = params.get('departure_city', None)
        start_date = params.get('start_date', None)
        end_date = params.get('end_date', None)
        price_start = params.get('price_start', None)
        price_end = params.get('price_end', None)
        hotel = params.get('hotel', None)
        hotel_city = params.get('hotel_city', None)
        hotel_ranks = params.get('hotel_ranks', None)
        nutritions = params.get('nutritions', None)
        night_from = params.get('night_from', None)
        night_to = params.get('night_to', None)

        qs = TourPackage.objects.filter(is_active=True)

        if departure_city:
            qs = qs.filter(flight__place_of_departure_1__icontains=departure_city)
        
        if night_from and night_to:
            qs = qs.filter(flight__departure_time_1__range=[night_from, night_to])

        if start_date:
            qs = qs.filter(start_date__gte=start_date)

        if end_date:
            qs = qs.filter(end_date__lte=end_date)

        if price_start and price_end:
            qs = qs.filter(price_for_person__range=[price_start, price_end])
        
        if hotel:
            qs = qs.filter(hotel__title__icontains=hotel)

        if hotel_city:
            qs = qs.filter(hotel__city__in=[hotel_city for hotel_city in hotel_city.split(',')])

        if hotel_ranks:
            qs = qs.filter(hotel__number_of_stars__in=[rank for rank in hotel_ranks.split(',')])

        if nutritions:
            qs = qs.filter(hotel__nutrition__in=[nutrition for nutrition in nutritions.split(',')])

        return qs

tourpackage_landing_search_api_view = TourPackageLandingSearchAPIView.as_view()


class DashboardAPIView(CustomListView):
    queryset = TourPackage.objects.filter(is_active=True)
    serializer_class = TourPackageSerializer

    def get_queryset(self):
        queryset = TourPackage.objects.filter(is_active=True)
        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')
        if month and year:
            queryset = queryset.filter(
                Q(start_date__month__gte=month, start_date__year__gte=year) |
                Q(start_date__month__lte=month, start_date__year__lte=year)
                )
        elif month:
            queryset = queryset.filter(
                Q(start_date__month__gte=month) |
                Q(start_date__month__lte=month)
            ) 
        elif year:
            queryset = queryset.filter(
                Q(start_date__year__gte=year) |
                Q(start_date__year__lte=year)
                )
        return queryset


    def get(self, *args, **kwargs):
        queryset = TourPackage.objects.select_related('flight').filter(is_active=True)
        data= []
        
        for tourpackage in queryset:
            hotel_titles = [hotel.title for hotel in tourpackage.hotel.all()]
            transport_titles = [transport.transport_type for transport in tourpackage.transport.all()]
            guides = [guide.full_name for guide in tourpackage.guide.all()]
            clients = Client.objects.filter(tour_package=tourpackage).count()
            
            id = tourpackage.id,
            guid = tourpackage.guid
            title = tourpackage.title
            flight_1 = tourpackage.flight.aviacompany_name_1
            flight_2 = tourpackage.flight.aviacompany_name_2
            flight_3 = tourpackage.flight.aviacompany_name_3
            flight_4 = tourpackage.flight.aviacompany_name_4
            number_of_seats = tourpackage.number_of_seats
            price_for_person = tourpackage.price_for_person
            start_date = tourpackage.start_date
            end_date = tourpackage.end_date
            status = tourpackage.status

            package_data = {
                "id": id,
                'guid': guid,
                "title": title,
                "flight_1": flight_1,
                "flight_2": flight_2,
                "flight_3": flight_3,
                "flight_4": flight_4,
                "transport": transport_titles,
                "hotel": hotel_titles,
                "clients": clients,
                'guide': guides,
                "number_of_seats": number_of_seats,
                "price_for_person": price_for_person,
                "start_date": start_date,
                "end_date": end_date,
                "status": status
            }
            data.append(package_data)
        return Response(data)
    
dashboard_api_view = DashboardAPIView.as_view()

from django.db.models import Prefetch
from ..outfit.models import OutfitType
from decimal import Decimal



class ReportDataAPIView(generics.ListAPIView):
    queryset = TourPackage.objects.filter(is_active=True)
    serializer_class = TourPackageSerializer

    def get_queryset(self):
        queryset = TourPackage.objects.filter(is_active=True).select_related(
            'flight', 
            'manager'
            ).prefetch_related(
            'hotel',
            'outfit',
            'transport'
            )
        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')
        if month and year:
            queryset = queryset.filter(
                Q(start_date__month=month, start_date__year=year) |
                Q(start_date__month=month, start_date__year=year)
                )
        elif month:
            queryset = queryset.filter(
                Q(start_date__month=month) |
                Q(start_date__month=month)
            ) 
        elif year:
            queryset = queryset.filter(
                Q(start_date__year=year) |
                Q(start_date__year=year)
                )
        return queryset
    
    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        data = []

        for tourpackage in queryset:
            hotel_title = [hotel.title for hotel in tourpackage.hotel.all()]
            # hotel_start_date = [hotel.start_date for hotel in tourpackage.hotel.all()] 
            # hotel_end_date = [hotel.end_date for hotel in tourpackage.hotel.all()] 
            hotel_nights = [int(hotel.booking_duration) for hotel in tourpackage.hotel.all()] 
            number_of_room = [hotel.number_of_room for hotel in tourpackage.hotel.all()]
            clients = Client.objects.filter(tour_package=tourpackage).select_related('tour_package').count()
            outfit_price = [outfit.outfit_type.price_for_one for outfit in tourpackage.outfit.all()] 
            total_price = sum(outfit_price)
            first_expense = total_price * clients

            each_room_type_count = tourpackage.hotel_data
            client_count_by_room_type = []

            for hotel in each_room_type_count:
                room_counts = []
                for i in range(1, 5):  # Assuming there are room_1_count to room_4_count keys
                    room_count_key = f'rooms_{i}_count'
                    room_counts.append(hotel.get(room_count_key, 0))
                client_count_by_room_type.append(room_counts)

            print('room_counts_list', client_count_by_room_type)

            flight_calculations = tourpackage.flight.calculations.all()
            total_amount = sum(calculation.total_amount for calculation in flight_calculations)
            ticket_price = total_amount
            service_price = clients * 24

            other_expenses = OtherExpense.objects.filter(tourpackage=tourpackage).select_related('tourpackage')
            drug_amount=0
            for other_expense in other_expenses:
                drug_amount += other_expense.amount

            tourpackage_title = tourpackage.title
            place_of_arrival_1 = tourpackage.flight.place_of_arrival_1
            place_of_departure_1 = tourpackage.flight.place_of_departure_1
            place_of_arrival_2 = tourpackage.flight.place_of_arrival_2
            place_of_departure_2 = tourpackage.flight.place_of_departure_2
            place_of_arrival_3 = tourpackage.flight.place_of_arrival_3
            place_of_departure_3 = tourpackage.flight.place_of_departure_3
            place_of_arrival_4 = tourpackage.flight.place_of_arrival_4
            place_of_departure_4 = tourpackage.flight.place_of_departure_4
            landing_date_1 = tourpackage.flight.landing_time_1
            departure_date_1 = tourpackage.flight.departure_time_1
            landing_date_2 = tourpackage.flight.landing_time_2
            departure_date_2 = tourpackage.flight.departure_time_2
            landing_date_3 = tourpackage.flight.landing_time_3
            departure_date_3 = tourpackage.flight.departure_time_3
            landing_date_4 = tourpackage.flight.landing_time_4
            departure_date_4 = tourpackage.flight.departure_time_4

            landing_date_1_format = None 
            landing_date_2_format = None 
            landing_date_3_format = None 
            landing_date_4_format = None 
            departure_date_1_format = None 
            departure_date_2_format = None 
            departure_date_3_format = None 
            departure_date_4_format = None 

            if landing_date_1 is not None:
                landing_date_1_format = (datetime.fromisoformat(str(landing_date_1)).astimezone(timezone.utc)).strftime('%d-%m-%Y')
            else:
                print("Date field is empty.", landing_date_1)
            if departure_date_1 is not None:
                departure_date_1_format = (datetime.fromisoformat(str(departure_date_1)).astimezone(timezone.utc)).strftime('%d-%m-%Y')
            else:
                print("Date field is empty.", departure_date_1)
            if landing_date_2 is not None:
                landing_date_2_format = (datetime.fromisoformat(str(landing_date_2)).astimezone(timezone.utc)).strftime('%d-%m-%Y')
            else:
                print("Date field is empty.", landing_date_2)
            if departure_date_2 is not None:
                departure_date_2_format = (datetime.fromisoformat(str(departure_date_2)).astimezone(timezone.utc)).strftime('%d-%m-%Y')
            else:
                print("Date field is empty.", departure_date_2)
            if landing_date_3 is not None:
                landing_date_3_format = (datetime.fromisoformat(str(landing_date_3)).astimezone(timezone.utc)).strftime('%d-%m-%Y')
            else:
                print("Date field is empty.", landing_date_3)
            if departure_date_3 is not None:    
                departure_date_3_format = (datetime.fromisoformat(str(departure_date_3)).astimezone(timezone.utc)).strftime('%d-%m-%Y')
            else:
                print("Date field is empty.", departure_date_3)
            if landing_date_4 is not None:  
                landing_date_4_format = (datetime.fromisoformat(str(landing_date_4)).astimezone(timezone.utc)).strftime('%d-%m-%Y')
            else:
                print("Date field is empty.", landing_date_4)
            if departure_date_4 is not None: 
                departure_date_4_format = (datetime.fromisoformat(str(departure_date_4)).astimezone(timezone.utc)).strftime('%d-%m-%Y')
            else:
                print("Date field is empty.", departure_date_4)

            # date_only_1 = landing_date_1.date()
            # date_only_2 = departure_date_1.date()
            # night_difference = date_only_1 - date_only_2
            # nights = night_difference.days 

            benefits = Client.objects.filter(tour_package=tourpackage)
            benefit_amount=0
            for benefit in benefits:
                benefit_amount += benefit.total_amount

            hotel_clients = Client.objects.filter(tour_package=tourpackage)
            hotel_client_counts = {
                hotel.title: {
                    'single': hotel_clients.filter(room_type='single').count(),
                    'double': hotel_clients.filter(room_type='double').count(),
                    'triple': hotel_clients.filter(room_type='triple').count(),
                    'quad': hotel_clients.filter(room_type='quad').count(),
                }
                for hotel in tourpackage.hotel.all()
            }

            single_room_price = [hotel.single_room_price for hotel in tourpackage.hotel.all()]
            double_room_price = [hotel.double_room_price for hotel in tourpackage.hotel.all()]
            triple_room_price = [hotel.triple_room_price for hotel in tourpackage.hotel.all()]
            quadruple_room_price = [hotel.quadruple_room_price for hotel in tourpackage.hotel.all()]

            hotel_single_room_total_price = [price * hotel_client_counts[hotel.title]['single'] * nights for hotel, price, nights in zip(tourpackage.hotel.all(), single_room_price, hotel_nights)]
            hotel_double_room_total_price = [price * hotel_client_counts[hotel.title]['double'] * nights for hotel, price, nights in zip(tourpackage.hotel.all(), single_room_price, hotel_nights)]
            hotel_triple_room_total_price = [price * hotel_client_counts[hotel.title]['triple'] * nights for hotel, price, nights in zip(tourpackage.hotel.all(), single_room_price, hotel_nights)]
            hotel_quad_room_total_price = [price * hotel_client_counts[hotel.title]['quad'] * nights for hotel, price, nights in zip(tourpackage.hotel.all(), single_room_price, hotel_nights)]
            
            hotel_total_price = [
                sum(prices) for prices in zip(
                    hotel_single_room_total_price,
                    hotel_double_room_total_price,
                    hotel_triple_room_total_price,
                    hotel_quad_room_total_price
                )
            ]
            
            additional_expense_for_hotel = []
            if tourpackage.hotel_data:
                for item in tourpackage.hotel_data:
                    if "additional_expense" in item:
                        additional_expense_for_hotel.append(item["additional_expense"])
                    else:
                        additional_expense_for_hotel.append(0)
            else:
                additional_expense_for_hotel = [0] * tourpackage.hotel.count()

            # final_food_price = [
            #     clients * hotel_nights * expense for expense in additional_expense_for_hotel
            # ]

            # food_price_for_each_hotel = [
            #     price * nights
            #     for price, nights in zip(final_food_price, hotel_nights)
            # ]

            food_price_for_each_hotel = [
                clients * nights * expense
                for nights, expense in zip(hotel_nights, additional_expense_for_hotel)
            ]
                
            hotel_food_sum = [
                total_price + food_price
                for total_price, food_price in zip(hotel_total_price, food_price_for_each_hotel)
            ]

            currency = tourpackage.currency
            currency_usd = [round(value / currency, 2) if currency else 0 for value in hotel_food_sum]
            visas = Visa.objects.filter(tour_package=tourpackage)
            visa = 0
            for visa in visas:
                visa = visa.price_for_one

            visa_price = clients*visa

            total_expense_hotel_food = sum(currency_usd)
            total_expense = (
                total_expense_hotel_food +
                first_expense +
                ticket_price +
                visa_price +
                service_price +
                drug_amount
            )

            if clients != 0:
                for_one_person = total_expense / clients
            else:
                for_one_person = Decimal('0.00') 
            
            benefit_total_expense = benefit_amount - total_expense

            data_1 = {
                'tourpackage_id': tourpackage.id,
                'tourpackage_title': tourpackage_title,
                'hotel': hotel_title,
                # 'hotel_start_date': hotel_start_date,
                # 'hotel_end_date': hotel_end_date,
                'place_of_arrival_1': place_of_arrival_1,
                'place_of_departure_1': place_of_departure_1,
                'place_of_arrival_2': place_of_arrival_2,
                'place_of_departure_2': place_of_departure_2,
                'place_of_arrival_3': place_of_arrival_3,
                'place_of_departure_3': place_of_departure_3,
                'place_of_arrival_4': place_of_arrival_4,
                'place_of_departure_4': place_of_departure_4,
                'landing_date_1': landing_date_1_format,
                'departure_date_1': departure_date_1_format,
                'landing_date_2': landing_date_2_format,
                'departure_date_2': departure_date_2_format,
                'landing_date_3': landing_date_3_format,
                'departure_date_3': departure_date_3_format,
                'landing_date_4': landing_date_4_format,
                'departure_date_4': departure_date_4_format,
                # 'night': nights,
                'nights': hotel_nights,
                'clients': clients,
                'outfit_price': outfit_price,
                'first_expense': first_expense,
                'ticket_price': ticket_price,
                'visa_price': visa_price,
                'service_price': service_price,
                'otper_expense': drug_amount,
                'number_of_room': number_of_room,
                'single_room_price': single_room_price,
                'double_room_price': double_room_price,
                'triple_room_price': triple_room_price,
                'quadruple_room_price': quadruple_room_price,
                'hotel_single_room_total_price': hotel_single_room_total_price,
                'hotel_double_room_total_price': hotel_double_room_total_price,
                'hotel_triple_room_total_price': hotel_triple_room_total_price,
                'hotel_quad_room_total_price': hotel_quad_room_total_price,
                'hotel_total_price': hotel_total_price,
                'additional_expese_for_hotel': additional_expense_for_hotel,
                'food_price_for_each_hotel': food_price_for_each_hotel,
                'currency_usd': currency_usd,
                'total_expense_hotel_food': total_expense_hotel_food,
                'total_expense': total_expense,
                'for_one_person': for_one_person,
                'benefits': benefit_amount,
                'benefit_total_expense': benefit_total_expense,
                'hotel_client_counts': hotel_client_counts,
                'client_count_by_room_type': client_count_by_room_type
            }
            data.append(data_1)
        return Response(data)

    

report_data_api_view = ReportDataAPIView.as_view()


class TourPackageBookCreateAPIView(generics.CreateAPIView):
    queryset = TourPackageBook.objects.all()
    serializer_class = TourPackageBookCreateSerializer

tourpackage_book_create_api_view = TourPackageBookCreateAPIView.as_view()


class TourPackageBookListAPIView(CustomListView):
    queryset = TourPackageBook.objects.all()
    serializer_class = TourPackageBookListSerializer

tourpackage_book_list_api_view = TourPackageBookListAPIView.as_view()


class TourPackageBookUpdateAPIView(generics.UpdateAPIView):
    queryset = TourPackageBook.objects.all()
    serializer_class = TourPackageBookUpdateSerializer
    lookup_field = 'guid'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Successfully updated'})
        return Response({'message': 'failed', 'details': serializer.errors})

tourpackage_book_update_api_view = TourPackageBookUpdateAPIView.as_view()


class ContactListAPIView(CustomListView):
    queryset = Contact.objects.all()
    serializer_class = ContanctSerializer

contact_list_api_view = ContactListAPIView.as_view()


class ContactUpdteAPIView(generics.UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContanctSerializer
    lookup_field = 'guid'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'success'})
        return Response({'message': 'failed', 'details': serializer.errors})

contact_update_api_view = ContactUpdteAPIView.as_view()


class FastContactCreateAPIView(generics.CreateAPIView):
    queryset = FastContact.objects.all()
    serializer_class = FastContanctSerializer

fast_contact_create_api_view = FastContactCreateAPIView.as_view()


class FastContactUpdteAPIView(generics.UpdateAPIView):
    queryset = FastContact.objects.all()
    serializer_class = FastContactUpdateSerializer
    lookup_field = 'guid'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'success'})
        return Response({'message': 'failed', 'details': serializer.errors})

fast_contact_update_api_view = FastContactUpdteAPIView.as_view()


class FastContactListAPIView(CustomListView):
    queryset = FastContact.objects.all()
    serializer_class = FastContanctSerializer

fast_contact_list_api_view = FastContactListAPIView.as_view()


class LandingDataListAPIView(CustomListView):
    queryset = LandingData.objects.all()
    serializer_class = LandingDataSerializer

landing_data_list_api_view = LandingDataListAPIView.as_view()



class LandingDataListAPIView(APIView):
    queryset = LandingData.objects.all()
    serializer_class = LandingDataSerializer

    def get(self, request, guid):
        instance = LandingData.objects.get(guid=guid)
        serializer = LandingDataSerializer(instance)
        return Response(serializer.data)


    def post(self, request):
        serializer = LandingDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, guid):
        instance = LandingData.objects.get(guid=guid)
        serializer = LandingDataSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, guid):
        instance = LandingData.objects.get(guid=guid)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

landing_create_put_list_api_view = LandingDataListAPIView.as_view()