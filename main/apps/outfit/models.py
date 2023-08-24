from django.db import models
from django.utils.translation import gettext as _
from ..common.models import BaseModel, BaseMeta


class OutfitTypeChoices(models.TextChoices):
    Kamzul = 'Kamzul', _('Kamzul')
    Qol_sumka = "Qo'l sumka", _("Qo'l sumka")
    Yon_sumka = 'Yon sumka', _('Yon sumka')
    Beyjik = 'Beyjik', _('Beyjik')
    Romol = "Ro'mol", _("Ro'mol")
    Futbolka = 'Futbolka', _('Futbolka')
    Pinka_koylak = "Pinka ko'ylak", _("Pinka ko'ylak")
    Exrom = "Exrom", _("Exrom")
    Bagach_sumka = 'Bagach sumka', _('Bagach sumka')
    Yaxtak_shalvar = "Yaxtak va Shalvar", _("Yaxtak va Shalvar")
    Ofis_sovgasi = "Ofis sovg'asi", _("Ofis sovg'asi")


class OutfitType(BaseModel):
    outfit_company = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=100, choices=OutfitTypeChoices.choices)
    number_of_outfit = models.PositiveIntegerField(default=0)
    price_for_one = models.DecimalField(max_digits=20, decimal_places=2)
    data = models.JSONField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta(BaseMeta):
        verbose_name = _("OutfitType")
        verbose_name_plural = _("OutfitTypes")


    def __str__(self):
        return f'{self.title}'


class Outfit(BaseModel):
    outfit_type = models.ForeignKey(OutfitType, on_delete=models.DO_NOTHING)
    full_name = models.CharField(max_length=100, blank=True)


    class Meta(BaseMeta):
        verbose_name = _("Outfit")
        verbose_name_plural = _("Outfits")


    def __str__(self):
        return f'{self.id}'
    
    
    def delete(self, *args, **kwargs):
        if self.tourpackage_set.exists():
            raise models.ProtectedError("This outfit is associated with tour packages.", self)
        super().delete(*args, **kwargs) 
    

class OutfitCalculation(BaseModel):
    outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    number_of_items = models.PositiveIntegerField(default=0)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    prepayment = models.DecimalField(max_digits=20, decimal_places=2)
    remained_amount = models.DecimalField(max_digits=20, decimal_places=2)


    class Meta(BaseMeta):
        verbose_name = _("OutfitCalculation")
        verbose_name_plural = _("OutfitCalculations")


    def __str__(self):
        return f'{self.id}'
        
    
    
class FastContact(BaseModel):
    full_name = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    is_viewed = models.BooleanField(default=False)

    class Meta(BaseMeta):
        verbose_name = _("FastContact")
        verbose_name_plural = _("FastContact")


    def __str__(self):
        return f'{self.full_name}'
