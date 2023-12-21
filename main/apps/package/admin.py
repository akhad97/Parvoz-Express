from django.contrib import admin
from .models import (
    TourPackage, 
    Contact,
    TourPackageBook,
    LandingData,
    TourpackageExpense,
    MonthlyExpense
)



class TourPackageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "guid", 
        "title", 
        "start_date", 
        "end_date", 
        "number_of_seats",
        "price_for_person"
        )
    list_display_links = ('id' ,"guid",)
    search_fields = ["title", ]

admin.site.register(TourPackage, TourPackageAdmin)


class TourPackaBookgeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "guid", 
        "full_name", 
        "phone_number"
        )
    list_display_links = ('id' ,"guid",)
    search_fields = ["full_name", ]

admin.site.register(TourPackageBook, TourPackaBookgeAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "guid", 
        "phone_number_1", 
        "phone_number_2"
        )
    list_display_links = ('id' ,"guid",)

admin.site.register(Contact, ContactAdmin)


class LandingDataAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "guid", 
        "title", 
        "sub_title"
        )
    list_display_links = ('id' ,"guid",)
    search_fields = ["title", ]

admin.site.register(LandingData, LandingDataAdmin)
admin.site.register(MonthlyExpense)
admin.site.register(TourpackageExpense)