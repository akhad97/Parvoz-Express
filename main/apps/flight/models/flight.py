from django.db import models
from django.utils.translation import gettext as _
from ...common.models import BaseModel, BaseMeta



class FlightTypeChoices(models.TextChoices):
    Direct_flight = 'Direct flight', _('Direct flight')
    Charter_flight = 'Charter flight', _('Charter flight')


class FlightType(BaseModel):
    title = models.CharField(max_length=100, choices=FlightTypeChoices.choices)
    
    class Meta(BaseMeta):
        verbose_name = _('Flight Type')
        verbose_name_plural = _('Flight Types')
    
    def __str__(self):
        return f'{self.title}'


class Flight(BaseModel):
    flight_type = models.ForeignKey(FlightType, on_delete=models.DO_NOTHING)
    aviacompany_name_1 = models.CharField(max_length=100, null=True, blank=True)
    place_of_arrival_1 = models.CharField(max_length=100, null=True, blank=True)
    flight_name_1 = models.CharField(max_length=100, null=True, blank=True)
    number_of_seats_1 = models.IntegerField(null=True, blank=True)
    full_name_1 = models.CharField(max_length=100, null=True, blank=True)
    landing_date_1 = models.DateField(null=True, blank=True)
    landing_time_1 = models.DateTimeField(null=True, blank=True)
    day_of_week_1 = models.CharField(max_length=100, null=True, blank=True)
    place_of_departure_1 = models.CharField(max_length=100, null=True, blank=True)
    departure_date_1 = models.DateField(null=True, blank=True)
    departure_time_1 = models.DateTimeField(null=True, blank=True)
    phone_number_1 = models.CharField(max_length=50, null=True, blank=True)
    price_for_one = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    aviacompany_name_2 = models.CharField(max_length=100, null=True, blank=True)
    place_of_arrival_2 = models.CharField(max_length=100, null=True, blank=True)
    flight_name_2 = models.CharField(max_length=100, null=True, blank=True)
    number_of_seats_2 = models.IntegerField(null=True, blank=True)
    full_name_2 = models.CharField(max_length=100, null=True, blank=True)
    landing_date_2 = models.DateField(null=True, blank=True)
    landing_time_2 = models.DateTimeField(null=True, blank=True)
    day_of_week_2 = models.CharField(max_length=100, null=True, blank=True)
    place_of_departure_2 = models.CharField(max_length=100, null=True, blank=True)
    departure_date_2 = models.DateField(null=True, blank=True)
    departure_time_2 = models.DateTimeField(null=True, blank=True)
    phone_number_2 = models.CharField(max_length=50, null=True, blank=True)
    aviacompany_name_3 = models.CharField(max_length=100, null=True, blank=True)
    place_of_arrival_3 = models.CharField(max_length=100, null=True, blank=True)
    flight_name_3 = models.CharField(max_length=100, null=True, blank=True)
    number_of_seats_3 = models.IntegerField(null=True, blank=True)
    full_name_3 = models.CharField(max_length=100, null=True, blank=True)
    landing_date_3 = models.DateField(null=True, blank=True)
    landing_time_3 = models.DateTimeField(null=True, blank=True)
    day_of_week_3 = models.CharField(max_length=100, null=True, blank=True)
    place_of_departure_3 = models.CharField(max_length=100, null=True, blank=True)
    departure_date_3 = models.DateField(null=True, blank=True)
    departure_time_3 = models.DateTimeField(null=True, blank=True)
    phone_number_3 = models.CharField(max_length=50, null=True, blank=True)
    aviacompany_name_4 = models.CharField(max_length=100, null=True, blank=True)
    place_of_arrival_4 = models.CharField(max_length=100, null=True, blank=True)
    flight_name_4 = models.CharField(max_length=100, null=True, blank=True)
    number_of_seats_4 = models.IntegerField(null=True, blank=True)
    full_name_4 = models.CharField(max_length=100, null=True, blank=True)
    landing_date_4 = models.DateField(null=True, blank=True)
    landing_time_4 = models.DateTimeField(null=True, blank=True)
    day_of_week_4 = models.CharField(max_length=100, null=True, blank=True)
    place_of_departure_4 = models.CharField(max_length=100, null=True, blank=True)
    departure_date_4 = models.DateField(null=True, blank=True)
    departure_time_4 = models.DateTimeField(null=True, blank=True)
    phone_number_4 = models.CharField(max_length=50, null=True, blank=True)


    class Meta(BaseMeta):
        verbose_name = _('Flight')
        verbose_name_plural = _('Flights')

    def __str__(self):
        return f'{self.aviacompany_name_1}'


class FlightBook(BaseModel):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    is_viewed = models.BooleanField(default=False)


    class Meta(BaseMeta):
        verbose_name = _("FlightBook")
        verbose_name_plural = _("FlightBooks")


    def __str__(self):
        return f'{self.full_name}'