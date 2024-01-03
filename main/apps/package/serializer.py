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
from ..account.serializers import AgentCalculationSerializer



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
    
import json

class TourPackageSerializer(serializers.ModelSerializer):
    agentcalculations = AgentCalculationSerializer(many=True, read_only=True, source='agentcalculation_set')
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
            'agentcalculations',
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
        # request = self.context.get('request')
        # agent_id = request.query_params.get('agent_id')
        # agent_data = obj.agent_data
        # parsed_data = json.loads(agent_data)
        # agent_ids = [item.get('id') for item in parsed_data]
        # if int(agent_id) in agent_ids:
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




    