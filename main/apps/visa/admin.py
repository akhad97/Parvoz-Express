from django.contrib import admin
from .models import Visa, VisaCalculation


class VisaAdmin(admin.ModelAdmin):
    list_display = (
        "guid", 
        "tour_package", 
        "price_for_one", 
        "total_amount"
        )
    list_display_links = ("guid",)
    search_fields = ["tour_package", ]

admin.site.register(Visa, VisaAdmin)



class VisaCalculationAdmin(admin.ModelAdmin):
    list_display = (
        "guid", 
        "visa", 
        "from_date", 
        "to_date",
        "number_of_day"
        )
    list_display_links = ("guid",)
    search_fields = ["visa", ]

admin.site.register(VisaCalculation, VisaCalculationAdmin)