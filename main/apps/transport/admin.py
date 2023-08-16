from django.contrib import admin
from .models import Transport, TransportCalculation




class TransportAdmin(admin.ModelAdmin):
    list_display = ("guid", "transport_type", "city", "full_name")
    list_display_links = ("guid",)
    search_fields = ["id", "transport_type"]

admin.site.register(Transport, TransportAdmin)


class TransportCalculationAdmin(admin.ModelAdmin):
    list_display = ("guid", "transport")
    list_display_links = ("guid", 'transport')
    search_fields = ["id", "transport", 'from_date', 'to_date']

admin.site.register(TransportCalculation, TransportCalculationAdmin)