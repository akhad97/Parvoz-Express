from django.db import models

from ...common.models import BaseModel, BaseMeta
from django.utils.translation import gettext as _
from .flight import Flight


class FlightCalculation(BaseModel):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='calculations')
    from_date = models.DateField()
    to_date = models.DateField()
    number_of_seat = models.IntegerField()
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    prepayment = models.DecimalField(max_digits=20, decimal_places=2)
    remained_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)


    class Meta(BaseMeta):
        verbose_name = _("FlightCalculation")
        verbose_name_plural = _("FlightCalculations")


    def __str__(self):
        return f'{self.id}'