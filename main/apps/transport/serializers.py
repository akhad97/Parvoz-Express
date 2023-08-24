from rest_framework import serializers
from django.db.models import Sum

from .models import Transport, TransportCalculation



class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = (
            'id',
            'guid',
            'transport_type',
            'city',
            'image',
            'full_name',
            'is_active'
        )


class TransportCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = (
            'transport_type',
            'city',
            'image',
            'full_name'
        )



class TransportCalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportCalculation
        fields = (
            'id',
            'guid',
            'transport',
            'from_date',
            'to_date',
            'number_of_days',
            'total_amount',
            'prepayment',
            'remained_amount'
        )
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['remained_amount'] = instance.total_amount - instance.prepayment
        qs = TransportCalculation.objects.filter(transport=instance.transport)
        prepayment_sum = qs.aggregate(prepayment_sum=Sum('prepayment'))['prepayment_sum'] or 0
        remained_amount_sum = qs.aggregate(remained_amount_sum=Sum('remained_amount'))['remained_amount_sum'] or 0
        data['prepayment_sum'] = prepayment_sum
        data['remained_amount_sum'] = remained_amount_sum
        return data


class TransportCalculationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportCalculation
        fields = (
            'transport',
            'from_date',
            'to_date',
            'number_of_days',
            'total_amount',
            'prepayment',
            'remained_amount'
        )