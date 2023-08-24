from rest_framework import serializers 
from ...flight.models.calculation import FlightCalculation
from django.db.models import Sum


class FlightCalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightCalculation
        fields = (
            'id',
            'guid',
            'flight',
            'from_date',
            'to_date',
            'number_of_seat',
            'total_amount',
            'prepayment',
            'remained_amount'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['remained_amount'] = instance.total_amount - instance.prepayment
        qs = FlightCalculation.objects.filter(flight=instance.flight)
        prepayment_sum = qs.aggregate(prepayment_sum=Sum('prepayment'))['prepayment_sum'] or 0
        remained_amount_sum = qs.aggregate(remained_amount_sum=Sum('remained_amount'))['remained_amount_sum'] or 0
        data['prepayment_sum'] = prepayment_sum
        data['remained_amount_sum'] = remained_amount_sum
        return data



class FlightCalculationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightCalculation
        fields = (
            'flight',
            'from_date',
            'to_date',
            'number_of_seat',
            'total_amount',
            'prepayment',
            'remained_amount'
        )
