from rest_framework import serializers
from django.db.models import Sum
from .models import (
    Hotel, 
    HotelCalculation,
    HotelBook
)


class HotelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = (
            'id',
            'guid',
            'title',
            'city',
            'number_of_stars',
            'booking_duration',
            'number_of_floor',
            'number_of_room',
            'single_room_price',
            'double_room_price',
            'triple_room_price',
            'quadruple_room_price',
            'nutrition',
            'image',
            'data',
            'start_date',
            'end_date'
        )


class HotelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = (
            'title',
            'city',
            'number_of_stars',
            'booking_duration',
            'number_of_floor',
            'number_of_room',
            'single_room_price',
            'double_room_price',
            'triple_room_price',
            'quadruple_room_price',
            'nutrition',
            'image',
            'data',
            'start_date',
            'end_date'
        )



class HotelCalculationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelCalculation
        fields = (
            'id',
            'guid',
            'hotel',
            'from_date',
            'to_date',
            'quantity_by_room_type',
            'total_amount',
            'prepayment',
            'remained_amount'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['remained_amount'] = instance.total_amount - instance.prepayment
        qs = HotelCalculation.objects.filter(hotel=instance.hotel)
        prepayment_sum = qs.aggregate(prepayment_sum=Sum('prepayment'))['prepayment_sum'] or 0
        remained_amount_sum = qs.aggregate(remained_amount_sum=Sum('remained_amount'))['remained_amount_sum'] or 0
        data['prepayment_sum'] = prepayment_sum
        data['remained_amount_sum'] = remained_amount_sum
        return data


class HotelCalculationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelCalculation
        fields = (
            'hotel',
            'from_date',
            'to_date',
            'quantity_by_room_type',
            'total_amount',
            'prepayment',
            'remained_amount'
        )


class HotelBookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelBook
        fields = (
            'hotel',
            'full_name',
            'phone_number'
        )


class HotelBookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelBook
        fields = (
            'is_viewed',
        )

    def update(self, instance, validated_data):
        instance.is_viewed = validated_data.get('is_viewed', instance.is_viewed)
        instance.save()
        return instance


class HotelBookListSerializer(serializers.ModelSerializer):
    hotel_guid = serializers.CharField(source='hotel.guid')
    hotel_title = serializers.CharField(source='hotel.title')
    hotel_city = serializers.CharField(source='hotel.city')
    hotel_number_of_stars = serializers.CharField(source='hotel.number_of_stars')
    hotel_booking_duration = serializers.CharField(source='hotel.booking_duration')
    hotel_number_of_floor = serializers.CharField(source='hotel.number_of_floor')
    hotel_number_of_room = serializers.CharField(source='hotel.number_of_room')
    hotel_nutrition = serializers.CharField(source='hotel.nutrition')
    hotel_single_room_price = serializers.CharField(source='hotel.single_room_price')
    hotel_double_room_price = serializers.CharField(source='hotel.double_room_price')
    hotel_triple_room_price = serializers.CharField(source='hotel.triple_room_price')
    hotel_quad_room_price = serializers.CharField(source='hotel.quadruple_room_price')
    class Meta:
        model = HotelBook
        fields = (
            'hotel',
            'guid',
            'hotel_guid',
            'hotel_title',
            'hotel_city',
            'hotel_number_of_stars',
            'hotel_booking_duration',
            'hotel_number_of_floor',
            'hotel_number_of_room',
            'hotel_nutrition',
            'hotel_single_room_price',
            'hotel_double_room_price',
            'hotel_triple_room_price',
            'hotel_quad_room_price',
            'full_name',
            'phone_number',
            'is_viewed'
        )