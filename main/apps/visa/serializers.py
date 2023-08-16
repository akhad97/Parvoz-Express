from rest_framework import serializers
from django.db.models import Sum
from .models import (
    Visa, 
    VisaCalculation,
    VisaBook
)
from ..package.serializer import TourPackageSerializer



class VisaSerializer(serializers.ModelSerializer):
    tour_package = TourPackageSerializer()

    class Meta:
        model = Visa
        fields = (
            'id',
            'guid',
            'tour_package',
            'price_for_one',
            'total_amount'
        )


class VisaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visa
        fields = (
            'id',
            'guid',
            'tour_package',
            'price_for_one',
            'total_amount'
        )


class VisaCalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaCalculation
        fields = (
            'id',
            'guid',
            'visa',
            'from_date',
            'to_date',
            'number_of_day',
            'total_amount',
            'prepayment',
            'remained_amount'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        qs = VisaCalculation.objects.filter(visa=instance.visa)
        prepayment_sum = qs.aggregate(prepayment_sum=Sum('prepayment'))['prepayment_sum'] or 0
        remained_amount_sum = qs.aggregate(remained_amount_sum=Sum('remained_amount'))['remained_amount_sum'] or 0
        data['prepayment_sum'] = prepayment_sum
        data['remained_amount_sum'] = remained_amount_sum
        return data


class VisaCalculationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaCalculation
        fields = (
            'visa',
            'from_date',
            'to_date',
            'number_of_day',
            'total_amount',
            'prepayment',
            'remained_amount'
        )


class VisaBookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaBook
        fields = (
            'visa',
            'full_name',
            'phone_number'
        )


class VisaBookListSerializer(serializers.ModelSerializer):
    visa_guid = serializers.CharField(source='visa.guid')
    visa_tourpackage = serializers.CharField(source='visa.tourpackage')
    visa_tourpackage_title = serializers.CharField(source='visa.tourpackage.title')
    visa_price_for_one = serializers.CharField(source='visa.price_for_one')
    visa_total_amount = serializers.CharField(source='visa.total_amount')
    class Meta:
        model = VisaBook
        fields = (
            'visa',
            'visa_guid',
            'visa_tourpackage',
            'visa_tourpackage_title',
            'visa_price_for_one',
            'visa_total_amount',
            'full_name',
            'phone_number'
        )