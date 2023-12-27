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
from ..account.serializers import AgentListSerializer


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
    agent = AgentListSerializer(many=True)
    transport_full_names = serializers.SerializerMethodField()
    NMA1 = serializers.SerializerMethodField()
    NMA2 = serializers.SerializerMethodField()
    NMA3 = serializers.SerializerMethodField()
    NMA4 = serializers.SerializerMethodField()
    QQN = serializers.SerializerMethodField()
    MRN = serializers.SerializerMethodField()
    AZN = serializers.SerializerMethodField()
    TAS = serializers.SerializerMethodField()
    SKD = serializers.SerializerMethodField()

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
            'agent',
            'manager',
            'guide',
            'date_data',
            'outfit_data',
            'hotel_data',
            'agent_data',
            'status',
            'currency',
            'is_active',
            'transport_full_names',
            'NMA1',
            'NMA2',
            'NMA3',
            'NMA4',
            'QQN',
            'MRN',
            'AZN',
            'TAS',
            'SKD',
        )
    
    def get_NMA1(self, obj):
        NMA1 = Client.objects.filter(tour_package=obj, created_by='NMA1').count()
        return NMA1
    
    def get_NMA2(self, obj):
        NMA2 = Client.objects.filter(tour_package=obj, created_by='NMA2').count()
        return NMA2
    
    def get_NMA3(self, obj):
        NMA3 = Client.objects.filter(tour_package=obj, created_by='NMA3').count()
        return NMA3
    
    def get_NMA4(self, obj):
        NMA4 = Client.objects.filter(tour_package=obj, created_by='NMA4').count()
        return NMA4
    
    def get_QQN(self, obj):
        QQN = Client.objects.filter(tour_package=obj, created_by='QQN').count()
        return QQN
    
    def get_MRN(self, obj):
        MRN = Client.objects.filter(tour_package=obj, created_by='MRN').count()
        return MRN
    
    def get_AZN(self, obj):
        AZN = Client.objects.filter(tour_package=obj, created_by='AZN').count()
        return AZN
    
    def get_TAS(self, obj):
        TAS = Client.objects.filter(tour_package=obj, created_by='TAS').count()
        return TAS
    
    def get_SKD(self, obj):
        SKD = Client.objects.filter(tour_package=obj, created_by='SKD').count()
        return SKD
    

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
            'agent',
            'manager',
            'guide',
            'date_data',
            'outfit_data',
            'hotel_data',
            'agent_data',
            'status',
            'is_active',
            'currency'
        )

class TourPackagePriceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPackage
        fields = (
            'price_for_person',
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
            'agent',
            'manager',
            'guide',
            'date_data',
            'outfit_data',
            'hotel_data',
            'agent_data',
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
            'price_for_one',
            'group'
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
from decimal import Decimal

class FinanceDataSerializer(serializers.ModelSerializer):
    visa = serializers.SerializerMethodField()
    flight = serializers.SerializerMethodField()
    hotel = serializers.SerializerMethodField()
    hotel_food = serializers.SerializerMethodField()
    outfit = serializers.SerializerMethodField()
    num_of_client = serializers.SerializerMethodField()
    tourpackage_expense = serializers.SerializerMethodField()
    total_expense = serializers.SerializerMethodField()
    hotel_title = serializers.SerializerMethodField()
    flight_title_1 = serializers.CharField(source='flight.flight_name_1')
    flight_title_2 = serializers.CharField(source='flight.flight_name_2')
    flight_title_3 = serializers.CharField(source='flight.flight_name_3')
    flight_title_4 = serializers.CharField(source='flight.flight_name_4')
    # group = serializers.SerializerMethodField()

    class Meta:
        model = TourPackage
        fields = (
            'id',
            'guid',
            'title',
            'start_date',
            'end_date',
            'visa',
            'flight',
            'hotel',
            'hotel_food',
            'outfit',
            'num_of_client',
            'tourpackage_expense',
            'total_expense',
            'hotel_title',
            # 'group',
            'flight_title_1',
            'flight_title_2',
            'flight_title_3',
            'flight_title_4'
        )
    
    # def get_group(self, obj):
    #     tourpackage_expenses = list(TourpackageExpense.objects.filter(tourpackage=obj))
    #     for tourpackage_expense in tourpackage_expenses:
    #         return tourpackage_expense.group

    def get_hotel_title(self, obj):
        hotel_titles = obj.hotel.all() 
        return [hotel.title for hotel in hotel_titles]


    def get_tourpackage_expense(self, obj):
        expense = TourpackageExpense.objects.filter(tourpackage=obj).values(
            'id', 
            'guid', 
            'tourpackage', 
            'title', 
            'num_of_people', 
            'price_for_one',
            'group'
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
        num_of_client = obj.number_of_seats
        currency = obj.currency
        # num_of_client = Client.objects.filter(tour_package=obj).select_related('tour_package').count()
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
            ((num_of_client * nights * expense) / currency)
            for nights, expense in zip(hotel_nights, additional_expense_for_hotel)
        ]
        hotel_total_food = [round(value, 2) for value in food_price_for_each_hotel]
        return hotel_total_food


    def get_visa(self, obj):
        try:
            visa = Visa.objects.get(tour_package=obj)
            num_of_client = obj.number_of_seats
            # num_of_client = Client.objects.filter(tour_package=obj).count()
            total = visa.price_for_one * num_of_client
            return total
        except Visa.DoesNotExist:
            return 0
    

    def get_flight(self, obj):
        flight = obj.flight 
        num_of_client = obj.number_of_seats
        # num_of_client = Client.objects.filter(tour_package=obj).count()
        total = flight.price_for_one * num_of_client
        return total


    def get_first_non_zero_value(self, values):
        for value in values:
            if value != 0:
                return value
        return 0


    def get_hotel(self, obj):
        hotel_nights = [int(hotel.booking_duration) for hotel in obj.hotel.all()]
        num_of_client = obj.number_of_seats
        hotel_single_room_price = [int(hotel.single_room_price) for hotel in obj.hotel.all()]
        hotel_double_room_price = [int(hotel.double_room_price) for hotel in obj.hotel.all()]
        hotel_triple_room_price = [int(hotel.triple_room_price) for hotel in obj.hotel.all()]
        hotel_quad_room_price = [int(hotel.quadruple_room_price) for hotel in obj.hotel.all()]
        currency = obj.currency

        # print('hotel_sinle_room_price', hotel_single_room_price)
        # print('hotel_double_room_price', hotel_double_room_price)
        # print('hotel_triple_room_price', hotel_triple_room_price)
        # print('hotel_quad_room_price', hotel_quad_room_price)
        # print('hotel_nights', hotel_nights)

        # if hotel_sinle_room_price == 0:
        #     # total = ((hotel_sinle_room_price * hotel_nights)/currency)/1
        #     hotel_sinle_room_price = 0
        #     # total = [((Decimal(nights) * room_price) / currency) / Decimal(1) for nights, room_price in zip(hotel_nights, hotel_sinle_room_price)]
        # else: 
        #     total = [((Decimal(nights) * room_price) / currency) / Decimal(1) for nights, room_price in zip(hotel_nights, hotel_sinle_room_price)]


        # if hotel_double_room_price == 0:
        #     hotel_double_room_price = 0
        #     # total = ((hotel_double_room_price * hotel_nights)/currency)/2
        #     # total = [((Decimal(nights) * room_price) / currency) / Decimal(2) for nights, room_price in zip(hotel_nights, hotel_double_room_price)]
        # else:
        #     total = [((Decimal(nights) * room_price) / currency) / Decimal(2) for nights, room_price in zip(hotel_nights, hotel_double_room_price)]

        # if hotel_triple_room_price == 0:
        #     hotel_triple_room_price = 0
        #     # total = ((hotel_triple_room_price * hotel_nights)/currency)/3
        #     # total = [((Decimal(nights) * room_price) / currency) / Decimal(3) for nights, room_price in zip(hotel_nights, hotel_triple_room_price)]
        # else:
        #     total = [((Decimal(nights) * room_price) / currency) / Decimal(3) for nights, room_price in zip(hotel_nights, hotel_triple_room_price)]
        #     print('total>>>>>', total)

        # if hotel_quad_room_price == 0:
        #     hotel_quad_room_price = 0
        #     # total = ((hotel_quad_room_price * hotel_nights)/currency)/3
        #     # total = [((Decimal(nights) * room_price) / currency) / Decimal(4) for nights, room_price in zip(hotel_nights, hotel_quad_room_price)]
        # else:
        #     total = [((Decimal(nights) * room_price) / currency) / Decimal(4) for nights, room_price in zip(hotel_nights, hotel_quad_room_price)]


        # non_zero_price = self.get_first_non_zero_value([
        #     self.get_first_non_zero_value(hotel_single_room_price),
        #     self.get_first_non_zero_value(hotel_double_room_price),
        #     self.get_first_non_zero_value(hotel_triple_room_price),
        #     self.get_first_non_zero_value(hotel_quad_room_price)
        # ])
        # print('non_zero_price', non_zero_price)

        tests = [hotel_single_room_price, hotel_double_room_price, hotel_triple_room_price, hotel_quad_room_price]
        non_zero_price = [0] * len(tests[0])
        for i in range(len(tests)):
            for x in range(len(tests[i])):
                price = tests[i][x]
                if price > 0:
                    non_zero_price[x] = price
                    print('non_zero_price', non_zero_price[x])
                
        if non_zero_price:
            room_type_divisors = {
                'single': 1,
                'double': 2,
                'triple': 3,
                'quad': 4
            }            

            room_type = None
            for room_type, room_prices in zip(room_type_divisors.keys(), [hotel_single_room_price, hotel_double_room_price, hotel_triple_room_price, hotel_quad_room_price]):
                if non_zero_price in room_prices:
                    break

            if room_type:
                total = [((Decimal(nights) * non_zero_price[x] * num_of_client) / currency) / Decimal(room_type_divisors[room_type]) for x, nights in enumerate(hotel_nights)]
            else:
                total = []
        else:
            total = []
        
        hotel_total = [round(value, 2) for value in total]
        return hotel_total


        # total = ((hotel_price * hotel_nights)/currency)/(2 or 3 or 4)
        # hotel_clients = Client.objects.filter(tour_package=obj)
        # hotel_client_counts = {
        #         hotel.title: {
        #             'single': hotel_clients.filter(room_type='single').count(),
        #             'double': hotel_clients.filter(room_type='double').count(),
        #             'triple': hotel_clients.filter(room_type='triple').count(),
        #             'quad': hotel_clients.filter(room_type='quad').count(),
        #         }
        #         for hotel in obj.hotel.all()
        # }
        # single_room_price = [hotel.single_room_price for hotel in obj.hotel.all()]
        # double_room_price = [hotel.double_room_price for hotel in obj.hotel.all()]
        # triple_room_price = [hotel.triple_room_price for hotel in obj.hotel.all()]
        # quadruple_room_price = [hotel.quadruple_room_price for hotel in obj.hotel.all()]

        # single_counts = [hotel_counts['single'] for hotel_counts in hotel_client_counts.values()]
        # double_counts = [hotel_counts['double'] for hotel_counts in hotel_client_counts.values()]
        # triple_counts = [hotel_counts['triple'] for hotel_counts in hotel_client_counts.values()]
        # quad_counts = [hotel_counts['quad'] for hotel_counts in hotel_client_counts.values()]

        # hotel_single_room_total_price = [price * count * nights for count, price, nights in zip(single_counts, single_room_price, hotel_nights)]
        # hotel_double_room_total_price = [price * count * nights for count, price, nights in zip(double_counts, double_room_price, hotel_nights)]
        # hotel_triple_room_total_price = [price * count * nights for count, price, nights in zip(triple_counts, triple_room_price, hotel_nights)]
        # hotel_quad_room_total_price = [price * count * nights for count, price, nights in zip(quad_counts, quadruple_room_price, hotel_nights)]

        # hotel_total_price = [
        #     sum(prices) for prices in zip(
        #         hotel_single_room_total_price,
        #         hotel_double_room_total_price,
        #         hotel_triple_room_total_price,
        #         hotel_quad_room_total_price
        #     )
        # ]
        # hotel_total_price = [nights * num_of_client * room_price for nights, room_price in zip(hotel_nights, hotel_room_price)]
        # hotel_total = [round(value, 2) for value in total]
        # return hotel_total

    
    def get_total_expense(self, obj):
        flight = self.get_flight(obj)
        visa = self.get_visa(obj)
        hotel = sum(self.get_hotel(obj))
        hotel_food = sum(self.get_hotel_food(obj))
        outfit = sum(item['price_for_one'] for item in self.get_outfit(obj))
        tourpackage_expense = sum(item['price_for_one'] for item in self.get_tourpackage_expense(obj))
        total_expense = flight + visa + hotel + hotel_food + outfit + tourpackage_expense 
        return total_expense
    


    


    