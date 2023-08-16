from django.db import models
from django.utils.translation import gettext as _
from ..common.models import BaseModel, BaseMeta
from ..package.models import TourPackage


class Visa(BaseModel):
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    price_for_one = models.DecimalField(max_digits=20, decimal_places=2)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta(BaseMeta):
        verbose_name = _("Visa")
        verbose_name_plural = _("Visas")

    def __str__(self):
        return f'{self.tour_package}'
    

class VisaCalculation(BaseModel):
    visa = models.ForeignKey(Visa, on_delete=models.CASCADE, related_name='visas')
    from_date = models.DateField()
    to_date = models.DateField()
    number_of_day = models.PositiveIntegerField(default=0)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    prepayment = models.DecimalField(max_digits=20, decimal_places=2)
    remained_amount = models.DecimalField(max_digits=20, decimal_places=2)


    class Meta(BaseMeta):
        verbose_name = _("VisaCalculation")
        verbose_name_plural = _("VisaCalculations")


    def __str__(self):
        return f'{self.visa}'
    

class VisaBook(BaseModel):
    visa = models.ForeignKey(Visa, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    is_viewed = models.BooleanField(default=False)


    class Meta(BaseMeta):
        verbose_name = _("VisaBook")
        verbose_name_plural = _("VisaBooks")


    def __str__(self):
        return f'{self.full_name}'