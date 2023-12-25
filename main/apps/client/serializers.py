from rest_framework import serializers
from .models import (
    Client, 
    Partner,
    VisaClient
)
from ..package.models import TourPackage


class ClientSerializer(serializers.ModelSerializer):
    hotel = serializers.SerializerMethodField()
    num_of_clients = serializers.SerializerMethodField()
    class Meta:
        model = Client
        fields = (
            'id',
            'guid',
            'tour_package',
            'hotel',
            'visa',
            'first_name',
            'last_name',
            'middle_name',
            'passport_series',
            'dob',
            'passport_expiration_date',
            'passport_img',
            'room_type',
            'total_amount',
            'remained_amount',
            'is_badge',
            'badge_file',
            'visa_file',
            'outfit_size',
            'human_development',
            'gender_type',
            'created_by',
            'contract_file',
            'num_of_clients'
        )
    
    def get_hotel(self, obj):
        hotel = obj.hotel
        if hotel is not None:
            return hotel.title
        else:
            return None

    def get_num_of_clients(self, obj):
        tour_package = obj.tour_package
        if isinstance(tour_package, TourPackage):
            client_counts = Client.objects.filter(tour_package=tour_package).count()
            return client_counts
        else:
            return 0
    

class ClientCreateSerializer(serializers.ModelSerializer):
    visa_file = serializers.FileField(required=False)
    class Meta:
        model = Client
        fields = (
            'id',
            'tour_package',
            'hotel',
            'visa',
            'first_name',
            'last_name',
            'middle_name',
            'passport_series',
            'dob',
            'passport_expiration_date',
            'passport_img',
            'room_type',
            'total_amount',
            'remained_amount',
            'is_badge',
            'badge_file',
            'visa_file',
            'outfit_size',
            'human_development',
            'gender_type',
            'created_by'
        )



class PartnerSerializer(serializers.ModelSerializer):
    visa_file = serializers.FileField(required=False)
    class Meta:
        model = Partner
        fields = (
            'id',
            'guid',
            'client',
            'first_name',
            'last_name',
            'middle_name',
            'passport_series',
            'dob',
            'passport_expiration_date',
            'passport_image',
            'total_amount',
            'remained_amount',
            'is_badge',
            'badge_file',
            'visa_file',
            'outfit_size',
            'human_development',
            'gender_type'
        )


class PartnerCreateSerializer(serializers.ModelSerializer):
    visa_file = serializers.FileField(required=False)
    class Meta:
        model = Partner
        fields = (
            'client',
            'first_name',
            'last_name',
            'middle_name',
            'passport_series',
            'dob',
            'passport_expiration_date',
            'passport_image',
            'total_amount',
            'remained_amount',
            'is_badge',
            'badge_file',
            'visa_file',
            'outfit_size',
            'human_development',
            'gender_type'
        )
        


class VisaClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaClient
        fields = (
            'id',
            'guid',
            'visa',
            'first_name',
            'last_name',
            'middle_name',
            'passport_series',
            'dob',
            'passport_expiration_date',
            'passport_img',
            'room_type',
            'total_amount',
            'remained_amount',
            'is_badge',
            'visa_file'
        )