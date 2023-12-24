from rest_framework import serializers
from django.db.models import Sum
from .models import (
    Manager, 
    Guide,
    ManagerCalculation,
    GuideCalculation
)


class ManagerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = (
            'id',
            'guid',
            'full_name',
            'nickname',
            'city',
            'phone_number',
            'price',
            'password',
            'is_active',
        )


class ManagerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = (
            'id',
            'guid',
            'full_name',
            'nickname',
            'city',
            'phone_number',
            'price',
            'password',
            'is_active',
        )

    def create(self, validated_data):
        validated_data['is_active'] = True
        return super().create(validated_data)


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = (
            'id',
            'guid',
            'full_name',
            'nickname',
            'city',
            'phone_number',
            'price',
            'manager',
            'password',
            'is_active'
        )
        
    def create(self, validated_data):
        validated_data['is_active'] = True
        return super().create(validated_data)


class ManagerCalculationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerCalculation
        fields = (
            'id',
            'guid',
            'manager',
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
        return data
    

class ManagerCalculationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerCalculation
        fields = (
            'manager',
            'from_date',
            'to_date',
            'quantity_by_room_type',
            'total_amount',
            'prepayment',
            'remained_amount'
        )


class GuideCalculationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuideCalculation
        fields = (
            'id',
            'guid',
            'guide',
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
        return data
    

class GuideCalculationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuideCalculation
        fields = (
            'guide',
            'from_date',
            'to_date',
            'quantity_by_room_type',
            'total_amount',
            'prepayment',
            'remained_amount'
        )


class GuideLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide 
        fields = (
            'id',
            'guid',
            'phone_number',
            'password'
        )


class ManagerLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager 
        fields = (
            'id',
            'guid',
            'phone_number',
            'password'
        )