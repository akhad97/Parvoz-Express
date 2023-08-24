from django.db import models
from ..common.models import BaseModel, BaseMeta
from django.utils.translation import gettext as _


class Manager(BaseModel):
    full_name = models.CharField(max_length=120)
    nickname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    is_active = models.BooleanField(default=True)

    class Meta(BaseMeta):
        verbose_name = _("Manager")
        verbose_name_plural = _("Managers")


    def __str__(self):
        return f'{self.full_name}'



class Guide(BaseModel):
    full_name = models.CharField(max_length=120)
    nickname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    manager = models.ForeignKey(Manager, on_delete=models.DO_NOTHING, related_name='managers')
    is_active = models.BooleanField(default=True)

    class Meta(BaseMeta):
        verbose_name = _("Guide")
        verbose_name_plural = _("Guides")


    def __str__(self):
        return f'{self.full_name}'
    

    def delete(self, *args, **kwargs):
        if self.tourpackage_set.exists():
            raise models.ProtectedError("This guide is associated with tour packages.", self)
        super().delete(*args, **kwargs) 

    

class ManagerCalculation(BaseModel):
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    quantity_by_room_type = models.PositiveIntegerField(default=0)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    prepayment = models.DecimalField(max_digits=20, decimal_places=2)
    remained_amount = models.DecimalField(max_digits=20, decimal_places=2)


    class Meta(BaseMeta):
        verbose_name = _("ManagerCalculation")
        verbose_name_plural = _("ManagerCalculations")


    def __str__(self):
        return f'{self.manager}'
    

class GuideCalculation(BaseModel):
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    quantity_by_room_type = models.PositiveIntegerField(default=0)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    prepayment = models.DecimalField(max_digits=20, decimal_places=2)
    remained_amount = models.DecimalField(max_digits=20, decimal_places=2)


    class Meta(BaseMeta):
        verbose_name = _("GuideCalculation")
        verbose_name_plural = _("GuideCalculations")


    def __str__(self):
        return f'{self.guide}'
