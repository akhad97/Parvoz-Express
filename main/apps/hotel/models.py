import os
from django.db import models
from django.utils.translation import gettext as _
from ..common.models import BaseModel, BaseMeta
from ..common.utils import upload_images


class NutritionTypeChoices(models.TextChoices):
    AI = 'AI', _('AI')
    BB = 'BB', _('BB')
    FB = 'FB', _('FB')
    HB = 'HB', _('HB')
    HBT = 'HBT', _('HBT')
    FBT = 'FBT', _('FBT')


class RATEChoices(models.IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5


class Hotel(BaseModel):
    title = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    number_of_stars = models.IntegerField(choices=RATEChoices.choices, default=RATEChoices.THREE)
    booking_duration = models.CharField(max_length=100)
    number_of_floor = models.PositiveIntegerField(default=0)
    number_of_room = models.PositiveIntegerField(default=0)
    nutrition = models.CharField(max_length=100, choices=NutritionTypeChoices.choices)
    image = models.ImageField(upload_to=upload_images(instance='self', path='hotel_images/'), null=True)
    single_room_price = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    double_room_price = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    triple_room_price = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    quadruple_room_price = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    data = models.JSONField(null=True, blank=True)


    class Meta(BaseMeta):
        verbose_name = _("Hotel")
        verbose_name_plural = _("Hotels")


    def __str__(self):
        return f'{self.title}'


class HotelCalculation(BaseModel):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    quantity_by_room_type = models.PositiveIntegerField(default=0)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    prepayment = models.DecimalField(max_digits=20, decimal_places=2)
    remained_amount = models.DecimalField(max_digits=20, decimal_places=2)


    class Meta(BaseMeta):
        verbose_name = _("HotelCalculation")
        verbose_name_plural = _("HotelCalculations")


    def __str__(self):
        return f'{self.id}'
    

class HotelBook(BaseModel):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    is_viewed = models.BooleanField(default=False)


    class Meta(BaseMeta):
        verbose_name = _("HotelBook")
        verbose_name_plural = _("HotelBooks")


    def __str__(self):
        return f'{self.full_name}'
