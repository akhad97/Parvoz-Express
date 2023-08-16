from rest_framework import serializers
from django.db.models import Sum
from .models import Outfit, OutfitType, OutfitCalculation



class OutfitTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutfitType
        fields = (
            'id',
            'guid',
            'outfit_company',
            'title',
            'number_of_outfit',
            'price_for_one',
            'data',
            'is_active'
        )


class OutfitTypeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutfitType
        fields = (
            'title',
            'outfit_company',
            'number_of_outfit',
            'price_for_one',
            'data'
        )

    
class OutfitListSerializer(serializers.ModelSerializer):
    outfit_type = OutfitTypeListSerializer()

    class Meta:
        model = Outfit
        fields = (
            'id',
            'guid',
            'outfit_type',
            'full_name'
        )
    

class OutfitCreateSerializer(serializers.ModelSerializer):
    outfit_type = OutfitTypeListSerializer()

    class Meta:
        model = Outfit
        fields = (
            'outfit_type',
            'full_name'
        )


class OutfitUpdateSerializer(serializers.ModelSerializer):
    outfit_type = OutfitTypeListSerializer()

    class Meta:
        model = Outfit
        fields = (
            'id',
            'outfit_type',
            'full_name'
        )

    def update(self, instance, validated_data):
        outfit_type_data = validated_data.pop('outfit_type', None)
        if outfit_type_data:
            outfit_type_serializer = OutfitTypeListSerializer(
                instance.outfit_type, data=outfit_type_data, partial=True
            )
            outfit_type_serializer.is_valid(raise_exception=True)
            outfit_type_instance = outfit_type_serializer.save()
            instance.outfit_type = outfit_type_instance

        instance = super().update(instance, validated_data)
        return instance
    

class OutfitCalculationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutfitCalculation
        fields = (
            'id',
            'outfit',
            'from_date',
            'to_date',
            'number_of_items',
            'total_amount',
            'prepayment',
            'remained_amount'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        qs = OutfitCalculation.objects.filter(outfit=instance.outfit)
        prepayment_sum = qs.aggregate(prepayment_sum=Sum('prepayment'))['prepayment_sum'] or 0
        remained_amount_sum = qs.aggregate(remained_amount_sum=Sum('remained_amount'))['remained_amount_sum'] or 0
        data['prepayment_sum'] = prepayment_sum
        data['remained_amount_sum'] = remained_amount_sum
        return data