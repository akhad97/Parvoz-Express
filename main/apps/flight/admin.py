from django.contrib import admin
from .models.flight import (
    Flight, 
    FlightType,
    FlightBook
)
from .models.calculation import FlightCalculation


class FlightBookAdmin(admin.ModelAdmin):
    list_display = (
        "id", 
        "guid", 
        "full_name", 
        "phone_number"
        )
    list_display_links = ("guid",)
    search_fields = ["full_name",]

admin.site.register(FlightBook, FlightBookAdmin)


class FlightAdmin(admin.ModelAdmin):
    list_display = (
        "guid", 
        "flight_type", 
        "aviacompany_name_1", 
        "place_of_arrival_1", 
        "flight_name_1"
        )
    list_display_links = ("guid",)
    search_fields = ["flight_type", "flight_name_1"]

admin.site.register(Flight, FlightAdmin)


class FlightTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        "guid", 
        "title", 
        )
    list_display_links = ("guid",)
admin.site.register(FlightType, FlightTypeAdmin)


class FlightCalculationAdmin(admin.ModelAdmin):
    list_display = (
        "guid", 
        "flight", 
        "from_date", 
        "to_date", 
        "number_of_seat"
        )
    list_display_links = ("guid",)
    search_fields = ["flight", ]

admin.site.register(FlightCalculation, FlightCalculationAdmin)