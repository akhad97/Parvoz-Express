from rest_framework import serializers
from .models import (
    Client, 
    Partner,
    VisaClient,
    VisaPartner
)



class ClientSerializer(serializers.ModelSerializer):
    hotel = serializers.CharField(source='hotel.title')
    class Meta:
        model = Client
        fields = (
            'id',
            'guid',
            'tour_package',
            'hotel',
            'visa',
            'full_name',
            'dob',
            'passport_expiration_date',
            'series',
            'series_number',
            'passport_img',
            'room_type',
            'total_amount',
            'remained_amount',
            'is_badge',
            'visa_file',
            'outfit_size'
        )


class ClientCreateSerializer(serializers.ModelSerializer):
    visa_file = serializers.FileField(required=False)
    class Meta:
        model = Client
        fields = (
            'id',
            'tour_package',
            'hotel',
            'visa',
            'full_name',
            'dob',
            'passport_expiration_date',
            'series',
            'series_number',
            'passport_img',
            'room_type',
            'total_amount',
            'remained_amount',
            'is_badge',
            'visa_file',
            'outfit_size'
        )



class PartnerSerializer(serializers.ModelSerializer):
    visa_file = serializers.FileField(required=False)
    class Meta:
        model = Partner
        fields = (
            'id',
            'guid',
            'client',
            'full_name',
            'dob',
            'passport_expiration_date',
            'series',
            'series_number',
            'passport_image',
            'total_amount',
            'remained_amount',
            'is_badge',
            'visa_file',
            'outfit_size'
        )


class PartnerCreateSerializer(serializers.ModelSerializer):
    visa_file = serializers.FileField(required=False)
    class Meta:
        model = Partner
        fields = (
            'client',
            'full_name',
            'dob',
            'passport_expiration_date',
            'series',
            'series_number',
            'passport_image',
            'total_amount',
            'remained_amount',
            'is_badge',
            'visa_file',
            'outfit_size'
        )
        


class VisaClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaClient
        fields = (
            'id',
            'guid',
            'visa',
            'full_name',
            'dob',
            'passport_expiration_date',
            'series',
            'series_number',
            'passport_img',
            'room_type',
            'total_amount',
            'remained_amount',
            'is_badge',
            'visa_file'
        )