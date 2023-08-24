from django.db import models
from django.utils.translation import gettext as _
from ..common.models import BaseModel, BaseMeta
from ..common.utils import upload_images


class TransportTypeChoices(models.TextChoices):
    Bus = 'Bus', _('Bus')
    Microbus = 'Microbus', _('Microbus')
    Taxi = 'Taxi', _('Taxi')
    Train = 'Train', _('Train')
 

class Transport(BaseModel):
    transport_type = models.CharField(max_length=100, choices=TransportTypeChoices.choices)
    city = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_images(path="transport_images/"), null=True)
    full_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)


    class Meta(BaseMeta):
        verbose_name = _("Transport")
        verbose_name_plural = _("Transports")


    def __str__(self):
        return f'{self.transport_type}'
    
    
    def delete(self, *args, **kwargs):
        if self.tourpackage_set.exists():
            raise models.ProtectedError("This transport is associated with tour packages.", self)
        super().delete(*args, **kwargs) 


class TransportCalculation(BaseModel):
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    number_of_days = models.IntegerField()
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    prepayment = models.DecimalField(max_digits=20, decimal_places=2)
    remained_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)


    class Meta(BaseMeta):
        verbose_name = _("TransportCalculation")
        verbose_name_plural = _("TransportCalculations")


    def __str__(self):
        return f'{self.id}'
    
    