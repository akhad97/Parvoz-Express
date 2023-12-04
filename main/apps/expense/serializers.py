from rest_framework import serializers
from .models import OtherExpense


class OtherExpenseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherExpense
        fields = (
            'id',
            'guid',
            'transport',
            'hotel',
            'outfit',
            'flight',
            'guide',
            'tourpackage',
            'title',
            'description',
            'amount',
            'confirmed'
        )


class OtherExpenseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherExpense
        fields = (
            'transport',
            'hotel',
            'outfit',
            'flight',
            'guide',
            'tourpackage',
            'title',
            'description',
            'amount',
            'confirmed'
        )


class TourpackageOtherExpenseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherExpense
        fields = (
            'tourpackage',
            'title',
            'description',
            'amount'
        )