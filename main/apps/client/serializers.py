from rest_framework import serializers
from .models import (
    Client, 
    Partner,
    VisaClient,
    VisaPartner
)


class ClientSerializer(serializers.ModelSerializer):
    hotel = serializers.SerializerMethodField()
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
            'created_by'
        )
    
    def get_hotel(self, obj):
        hotel = obj.hotel
        if hotel is not None:
            return hotel.title
        else:
            return None


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