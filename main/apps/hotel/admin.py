from django.contrib import admin
from .models import (
    Hotel, 
    HotelCalculation,
    HotelBook
)



class HotelAdmin(admin.ModelAdmin):
    list_display = ("guid", "title", "city", "number_of_stars")
    list_display_links = ("guid",)
    search_fields = ["title", ]

admin.site.register(Hotel, HotelAdmin)


class HotelBookAdmin(admin.ModelAdmin):
    list_display = ("id", "guid", "full_name", "phone_number")
    list_display_links = ("guid",)
    search_fields = ["full_name", ]

admin.site.register(HotelBook, HotelBookAdmin)


class HotelCalculationAdmin(admin.ModelAdmin):
    list_display = ("guid", "hotel", "total_amount", "prepayment", "remained_amount")
    list_display_links = ("guid",)
    search_fields = ["id", ]

admin.site.register(HotelCalculation, HotelCalculationAdmin)