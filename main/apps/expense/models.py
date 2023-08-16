from django.db import models
from django.utils.translation import gettext as _
from ..common.models import BaseModel, BaseMeta
from ..flight.models.flight import Flight
from ..transport.models import Transport
from ..hotel.models import Hotel
from ..employee.models import Guide
from ..outfit.models import Outfit
from ..package.models import TourPackage

# class CategoryChoices(models.TextChoices):
#     Transport = 'Transport', _('Transport')
#     Hotel = 'Hotel', _('Hotel')
#     Guide = 'Guide', _('Guide')
#     Outfit = 'Outfit', _('Outfit')
#     Flight = 'Flight', _('Flight')
#     TourPackage = 'TourPackage', _('TourPackage')


# class Category(BaseModel):

    

class OtherExpense(BaseModel):
    tourpackage = models.ForeignKey(TourPackage, on_delete=models.CASCADE, null=True)
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, related_name='hotel_calculations')
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, null=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=True)
    outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.DecimalField(max_digits=20, decimal_places=2)


    class Meta(BaseMeta):
        verbose_name = _("OtherExpense")
        verbose_name_plural = _("OtherExpenses")


    def __str__(self):
        return f'{self.id}'
    


def calculate_category_percentages():
    entity_counts = {
        'tourpackage': 0,
        'transport': 0,
        'hotel': 0,
        'guide': 0,
        'flight': 0,
        'outfit': 0,
    }
    total_expenses = 0

    # Loop through each entity type and count the expenses for it
    for entity_type in entity_counts.keys():
        expenses = OtherExpense.objects.filter(**{f'{entity_type}__isnull': False})
        entity_counts[entity_type] = expenses.count()
        total_expenses += expenses.count()

    entity_percentages = {}
    for entity_type, count in entity_counts.items():
        percentage = round((count / total_expenses) * 100, 2)
        entity_percentages[entity_type] = percentage

    return entity_percentages


# Usage example
# category_percentages = calculate_category_percentages()

# for category, percentage in category_percentages.items():
#     print(f"{category}: {percentage}%")
