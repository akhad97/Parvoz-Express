from rest_framework import serializers 
from .models import (
    TourPackage, 
    TourPackageBook, 
    Contact,
    LandingData,
    TourpackageExpense,
    MonthlyExpense
)
from ..outfit.models import FastContact
from ..hotel.serializers import HotelListSerializer
from ..outfit.serializers import OutfitListSerializer
from ..transport.serializers import TransportSerializer
from ..flight.serializer.flight import FlightSerializer
from ..employee.serializers import GuideSerializer


class TourPackageManagerGuideSerializer(serializers.ModelSerializer):
    client_count = serializers.SerializerMethodField()
    class Meta:
        model = TourPackage
        fields = (
            'id',
            'guid',
            'title',
            'start_date',
            'end_date',
            'client_count',
            'is_active'
        )

    def get_client_count(self, obj):
        return obj.tourpackage_clients.count()
    


class TourPackageSerializer(serializers.ModelSerializer):
    flight = FlightSerializer()
    hotel = HotelListSerializer(many=True)
    outfit = OutfitListSerializer(many=True)
    transport = TransportSerializer(many=True)
    guide = GuideSerializer(many=True)
    transport_full_names = serializers.SerializerMethodField()

    class Meta:
        model = TourPackage
        fields = (
            'id',
            'guid',
            'title',
            'start_date',
            'end_date',
            'additional_expense',
            'number_of_seats',
            'price_for_person',
            'flight',
            'hotel',
            'outfit',
            'transport',
            'manager',
            'guide',
            'date_data',
            'outfit_data',
            'hotel_data',
            'status',
            'currency',
            'is_active',
            'transport_full_names'
        )

    def get_transport_full_names(self, obj):
        return [transport.full_name for transport in obj.transport.all()]


class TourPackageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPackage
        fields = (
            'id',
            'guid',
            'title',
            'start_date',
            'end_date',
            'additional_expense',
            'number_of_seats',
            'price_for_person',
            'flight',
            'hotel',
            'outfit',
            'transport',
            'manager',
            'guide',
            'date_data',
            'outfit_data',
            'hotel_data',
            'status',
            'is_active',
            'currency'
        )



class TourPackageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPackage
        fields = (
            'id',
            'guid',
            'title',
            'start_date',
            'end_date',
            'additional_expense',
            'number_of_seats',
            'price_for_person',
            'flight',
            'hotel',
            'outfit',
            'transport',
            'manager',
            'guide',
            'date_data',
            'outfit_data',
            'hotel_data',
            'currency',
            'status'
        )



class TourPackageAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPackage
        fields = (
            'id',
            'guid',
            'start_date',
            'end_date',
            'number_of_seats',
            'flight',
            'status',
            'is_active'
        )



class TourPackageBookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPackageBook
        fields = (
            'tourpackage',
            'full_name',
            'phone_number'
        )

class TourPackageBookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPackageBook
        fields = (
            'is_viewed',
        )

    def update(self, instance, validated_data):
        instance.is_viewed = validated_data.get('is_viewed', instance.is_viewed)
        instance.save()
        return instance

class TourPackageBookListSerializer(serializers.ModelSerializer):
    tourpackage_guid = serializers.CharField(source='tourpackage.guid')
    tourpackage_title = serializers.CharField(source='tourpackage.title')
    tourpackage_start_date = serializers.CharField(source='tourpackage.start_date')
    tourpackage_end_date = serializers.CharField(source='tourpackage.end_date')
    tourpackage_additional_expense = serializers.CharField(source='tourpackage.additional_expense')
    tourpackage_number_of_seats = serializers.CharField(source='tourpackage.number_of_seats')
    tourpackage_price_for_person = serializers.CharField(source='tourpackage.price_for_person')
    tourpackage_manager = serializers.CharField(source='tourpackage.manager')
    tourpackage_status = serializers.CharField(source='tourpackage.status')

    class Meta:
        model = TourPackageBook
        fields = (
            'guid',
            'tourpackage',
            'tourpackage_guid',
            'tourpackage_title',
            'tourpackage_start_date',
            'tourpackage_end_date',
            'tourpackage_additional_expense',
            'tourpackage_number_of_seats',
            'tourpackage_price_for_person',
            'tourpackage_manager',
            'tourpackage_status',
            'full_name',
            'phone_number',
            'is_viewed'
        )

class ContanctSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'id',
            'guid',
            'phone_number_1',
            'phone_number_2',
            'telegram',
            'instagram',
            'facebook',
            'youtube'
        )


class FastContanctSerializer(serializers.ModelSerializer):
    class Meta:
        model = FastContact
        fields = (
            'id',
            'guid',
            'full_name',
            'phone_number',
            'is_viewed'
        )


class FastContactUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FastContact
        fields = (
            'is_viewed',
        )

    def update(self, instance, validated_data):
        instance.is_viewed = validated_data.get('is_viewed', instance.is_viewed)
        instance.save()
        return instance
    

class LandingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingData
        fields = (
            'id',
            'guid',
            'title',
            'title_uz',
            'title_ru',
            'title_en',
            'sub_title',
            'sub_title_uz',
            'sub_title_ru',
            'sub_title_en',
            'landing_img'
        )


class TourPackageExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourpackageExpense
        fields = (
            'id',
            'guid',
            'tourpackage',
            'title',
            'num_of_people',
            'price_for_one'
        )

from django.db.models import Q, Sum

class MonthlyExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyExpense
        fields = (
            'id',
            'guid',
            'communal_expense',
            'employee_salary',
            'tax',
            'telephone',
            'meet',
            'taxi',
            'employee_salary_mecca',
            'field_1',
            'field_2',
            'field_3',
            'date',
            'margin'
        )
     

from ..visa.models import Visa
from ..client.models import Client
from ..package.models import TourpackageExpense

class FinanceDataSerializer(serializers.ModelSerializer):
    visa = serializers.SerializerMethodField()
    flight = serializers.SerializerMethodField()
    hotel = serializers.SerializerMethodField()
    hotel_food = serializers.SerializerMethodField()
    outfit = serializers.SerializerMethodField()
    num_of_client = serializers.SerializerMethodField()
    tourpackage_expense = serializers.SerializerMethodField()
    total_expense = serializers.SerializerMethodField()

    class Meta:
        model = TourPackage
        fields = (
            'id',
            'guid',
            'title',
            'start_date',
            'end_date',
            # 'transport',
            'visa',
            'flight',
            'hotel',
            'hotel_food',
            'outfit',
            'num_of_client',
            'tourpackage_expense',
            'total_expense'
        )


    def get_tourpackage_expense(self, obj):
        expense = TourpackageExpense.objects.filter(tourpackage=obj).values(
            'id', 
            'guid', 
            'tourpackage', 
            'title', 
            'num_of_people', 
            'price_for_one'
            )
        return expense


    def get_num_of_client(self, obj):
        # clients = Client.objects.filter(tour_package=obj).select_related('tour_package').count()
        clients = obj.number_of_seats
        return clients
    

    def get_outfit(self, obj):
        outfits = [
        {"title": outfit.outfit_type.title, "price_for_one": outfit.outfit_type.price_for_one}
        for outfit in obj.outfit.all()
        ]
        return outfits
    

    def get_hotel_food(self, obj):
        hotel_nights = [int(hotel.booking_duration) for hotel in obj.hotel.all()]
        clients = Client.objects.filter(tour_package=obj).select_related('tour_package').count()
        additional_expense_for_hotel = []
        if obj.hotel_data:
            for item in obj.hotel_data:
                if "additional_expense" in item:
                    additional_expense_for_hotel.append(item["additional_expense"])
                else:
                    additional_expense_for_hotel.append(0)
        else:
            additional_expense_for_hotel = [0] * obj.hotel.count()
        food_price_for_each_hotel = [
            clients * nights * expense
            for nights, expense in zip(hotel_nights, additional_expense_for_hotel)
        ]
        return food_price_for_each_hotel


    def get_visa(self, obj):
        try:
            visa = Visa.objects.get(tour_package=obj)
            num_of_client = Client.objects.filter(tour_package=obj).count()
            total = visa.price_for_one * num_of_client
            return total
        except Visa.DoesNotExist:
            return 0
    

    def get_flight(self, obj):
        flight = obj.flight 
        num_of_client = Client.objects.filter(tour_package=obj).count()
        total = flight.price_for_one * num_of_client
        return total


    def get_hotel(self, obj):
        hotel_nights = [int(hotel.booking_duration) for hotel in obj.hotel.all()]
        # each_room_type_count = obj.hotel_data
        # client_count_by_room_type = []
        # for hotel in each_room_type_count:
        #     room_counts = []
        #     for i in range(1, 5): 
        #         room_count_key = f'rooms_{i}_count'
        #         room_counts.append(hotel.get(room_count_key, 0))
        #     client_count_by_room_type.append(room_counts)
        
        hotel_clients = Client.objects.filter(tour_package=obj)
        hotel_client_counts = {
                hotel.title: {
                    'single': hotel_clients.filter(room_type='single').count(),
                    'double': hotel_clients.filter(room_type='double').count(),
                    'triple': hotel_clients.filter(room_type='triple').count(),
                    'quad': hotel_clients.filter(room_type='quad').count(),
                }
                for hotel in obj.hotel.all()
            }

        single_room_price = [hotel.single_room_price for hotel in obj.hotel.all()]
        double_room_price = [hotel.double_room_price for hotel in obj.hotel.all()]
        triple_room_price = [hotel.triple_room_price for hotel in obj.hotel.all()]
        quadruple_room_price = [hotel.quadruple_room_price for hotel in obj.hotel.all()]
        
        # first_elements = []
        # for room_counts in client_count_by_room_type:
        #     first_element = room_counts[0] if room_counts else None
        #     first_elements.append(first_element)

        # second_elements = []
        # for room_counts in client_count_by_room_type:
        #     second_element = room_counts[1] if room_counts else None
        #     second_elements.append(second_element)

        # third_elements = []
        # for room_counts in client_count_by_room_type:
        #     third_element = room_counts[2] if room_counts else None
        #     third_elements.append(third_element)

        # fourth_elements = []
        # for room_counts in client_count_by_room_type:
        #     fourth_element = room_counts[3] if room_counts else None
        #     fourth_elements.append(fourth_element)

        single_counts = [hotel_counts['single'] for hotel_counts in hotel_client_counts.values()]
        double_counts = [hotel_counts['double'] for hotel_counts in hotel_client_counts.values()]
        triple_counts = [hotel_counts['triple'] for hotel_counts in hotel_client_counts.values()]
        quad_counts = [hotel_counts['quad'] for hotel_counts in hotel_client_counts.values()]

        hotel_single_room_total_price = [price * count * nights for count, price, nights in zip(single_counts, single_room_price, hotel_nights)]
        hotel_double_room_total_price = [price * count * nights for count, price, nights in zip(double_counts, double_room_price, hotel_nights)]
        hotel_triple_room_total_price = [price * count * nights for count, price, nights in zip(triple_counts, triple_room_price, hotel_nights)]
        hotel_quad_room_total_price = [price * count * nights for count, price, nights in zip(quad_counts, quadruple_room_price, hotel_nights)]


        # hotel_single_room_total_price = [price * first_element * nights for hotel, first_element, price, nights in zip(obj.hotel.all(), first_elements, single_room_price, hotel_nights)]
        # hotel_double_room_total_price = [price * second_element * nights for hotel, second_element, price, nights in zip(obj.hotel.all(), second_elements, double_room_price, hotel_nights)]
        # hotel_triple_room_total_price = [price * third_element * nights for hotel, third_element, price, nights in zip(obj.hotel.all(), third_elements, triple_room_price, hotel_nights)]
        # hotel_quad_room_total_price = [price * fourth_element * nights for hotel, fourth_element, price, nights in zip(obj.hotel.all(), fourth_elements, quadruple_room_price, hotel_nights)]

        hotel_total_price = [
            sum(prices) for prices in zip(
                hotel_single_room_total_price,
                hotel_double_room_total_price,
                hotel_triple_room_total_price,
                hotel_quad_room_total_price
            )
        ]
        return hotel_total_price

    
    def get_total_expense(self, obj):
        flight = self.get_flight(obj)
        visa = self.get_visa(obj)
        hotel = sum(self.get_hotel(obj))
        hotel_food = sum(self.get_hotel_food(obj))
        outfit = sum(item['price_for_one'] for item in self.get_outfit(obj))
        tourpackage_expense = sum(item['price_for_one'] for item in self.get_tourpackage_expense(obj))
        total_expense = flight + visa + hotel + hotel_food + outfit + tourpackage_expense 
        return total_expense
    


    


    