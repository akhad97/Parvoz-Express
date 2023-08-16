from rest_framework import serializers 
from ...flight.models.flight import (
    Flight, 
    FlightType,
    FlightBook
)


class FlightTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightType
        fields = (
            'id',
            'guid',
            'title'
        )


class FlightSerializer(serializers.ModelSerializer):
    departure_time_1 = serializers.DateTimeField(format="%d.%m.%Y %H:%M", required=False)
    landing_time_1 = serializers.DateTimeField(format="%d.%m.%Y %H:%M", required=False)
    departure_time_2 = serializers.DateTimeField(format="%d.%m.%Y %H:%M", required=False)
    landing_time_2 = serializers.DateTimeField(format="%d.%m.%Y %H:%M", required=False)
    departure_time_3 = serializers.DateTimeField(format="%d.%m.%Y %H:%M", required=False)
    landing_time_3 = serializers.DateTimeField(format="%d.%m.%Y %H:%M", required=False)
    departure_time_4 = serializers.DateTimeField(format="%d.%m.%Y %H:%M", required=False)
    landing_time_4 = serializers.DateTimeField(format="%d.%m.%Y %H:%M", required=False)
    class Meta:
        model = Flight
        fields = (
            'id',
            'guid',
            'flight_type',
            'aviacompany_name_1',
            'place_of_arrival_1',
            'flight_name_1',
            'number_of_seats_1',
            'full_name_1',
            'landing_time_1',
            'day_of_week_1',
            'place_of_departure_1',
            'departure_time_1',
            'phone_number_1',
            'flight_type',
            'aviacompany_name_2',
            'place_of_arrival_2',
            'flight_name_2',
            'number_of_seats_2',
            'full_name_2',
            'landing_time_2',
            'day_of_week_2',
            'place_of_departure_2',
            'departure_time_2',
            'phone_number_2',
            'flight_type',
            'aviacompany_name_3',
            'place_of_arrival_3',
            'flight_name_3',
            'number_of_seats_3',
            'full_name_3',
            'landing_time_3',
            'day_of_week_3',
            'place_of_departure_3',
            'departure_time_3',
            'phone_number_3',
            'flight_type',
            'aviacompany_name_4',
            'place_of_arrival_4',
            'flight_name_4',
            'number_of_seats_4',
            'full_name_4',
            'landing_time_4',
            'day_of_week_4',
            'place_of_departure_4',
            'departure_time_4',
            'phone_number_4',
        )

    

class FlightCreateSerializer(serializers.ModelSerializer):
    departure_time_1 = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Flight
        fields = (
            'flight_type',
            'aviacompany_name_1',
            'place_of_arrival_1',
            'flight_name_1',
            'number_of_seats_1',
            'full_name_1',
            'landing_date_1',
            'landing_time_1',
            'day_of_week_1',
            'place_of_departure_1',
            'departure_date_1',
            'departure_time_1',
            'phone_number_1',
            'flight_type',
            'aviacompany_name_2',
            'place_of_arrival_2',
            'flight_name_2',
            'number_of_seats_2',
            'full_name_2',
            'landing_date_2',
            'landing_time_2',
            'day_of_week_2',
            'place_of_departure_2',
            'departure_date_2',
            'departure_time_2',
            'phone_number_2',
            'flight_type',
            'aviacompany_name_3',
            'place_of_arrival_3',
            'flight_name_3',
            'number_of_seats_3',
            'full_name_3',
            'landing_date_3',
            'landing_time_3',
            'day_of_week_3',
            'place_of_departure_3',
            'departure_date_3',
            'departure_time_3',
            'phone_number_3',
            'flight_type',
            'aviacompany_name_4',
            'place_of_arrival_4',
            'flight_name_4',
            'number_of_seats_4',
            'full_name_4',
            'landing_date_4',
            'landing_time_4',
            'day_of_week_4',
            'place_of_departure_4',
            'departure_date_4',
            'departure_time_4',
            'phone_number_4',
        )



class FlightBookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightBook
        fields = (
            'flight',
            'full_name',
            'phone_number'
        )


class FlightBookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightBook
        fields = (
            'is_viewed',
        )

    def update(self, instance, validated_data):
        instance.is_viewed = validated_data.get('is_viewed', instance.is_viewed)
        instance.save()
        return instance


class FlightBookListSerializer(serializers.ModelSerializer):
    flight_guid = serializers.CharField(source='flight.guid')
    flight_place_of_departure_1 = serializers.CharField(source='flight.place_of_departure_1')
    flight_place_of_departure_2 = serializers.CharField(source='flight.place_of_departure_2')
    flight_place_of_departure_3 = serializers.CharField(source='flight.place_of_departure_3')
    flight_place_of_departure_4 = serializers.CharField(source='flight.place_of_departure_4')
    flight_departure_time_1 = serializers.CharField(source='flight.departure_time_1')
    flight_avia_company_name_1 = serializers.CharField(source='flight.aviacompany_name_1')
    flight_avia_company_name_3 = serializers.CharField(source='flight.aviacompany_name_3')
    
    class Meta:
        model = FlightBook
        fields = (
            'id',
            'guid',
            'flight',
            'flight_guid',
            'flight_place_of_departure_1',
            'flight_place_of_departure_2',
            'flight_place_of_departure_3',
            'flight_place_of_departure_4',
            'flight_departure_time_1',
            'flight_avia_company_name_1',
            'flight_avia_company_name_3',
            'full_name',
            'phone_number',
            'is_viewed'
        )