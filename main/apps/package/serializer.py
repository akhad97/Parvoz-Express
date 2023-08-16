from rest_framework import serializers 
from .models import TourPackage, TourPackageBook, Contact
from ..hotel.serializers import HotelListSerializer
from ..outfit.serializers import OutfitListSerializer
from ..transport.serializers import TransportSerializer
from ..flight.serializer.flight import FlightSerializer
from ..employee.serializers import GuideSerializer



class TourPackageSerializer(serializers.ModelSerializer):
    flight = FlightSerializer()
    hotel = HotelListSerializer(many=True)
    outfit = OutfitListSerializer(many=True)
    transport = TransportSerializer(many=True)
    guide = GuideSerializer(many=True)

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
            'is_active'
        )


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
            'is_active'
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
    # flight = FlightSerializer()
    # hotel = HotelListSerializer(many=True)
    # outfit = OutfitListSerializer(many=True)
    # transport = TransportSerializer(many=True)
    # guide = GuideSerializer(many=True)
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
            # 'flight',
            # 'hotel',
            # 'outfit',
            # 'transport',
            # 'guide',
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
            'title',
            'sub_title',
            'phone_number_1',
            'phone_number_2',
            'landing_img',
            'telegram',
            'instagram',
            'facebook',
            'youtube'
        )

