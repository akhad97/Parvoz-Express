from django.contrib import admin
from .models import (
    Outfit, 
    OutfitType, 
    OutfitCalculation,
    FastContact
)




class OutfitAdmin(admin.ModelAdmin):
    list_display = ("id", "outfit_company", "title", "number_of_outfit", "price_for_one")
    list_display_links = ("id",)
    search_fields = ["title", ]
    # list_filter = ("book", "title", "book_type")
    # list_editable = ("title", "book_type")

admin.site.register(OutfitType, OutfitAdmin)


class OutfitTypeAdmin(admin.ModelAdmin):
    list_display = ('id', "outfit_type", "full_name")
    list_display_links = ("id",)
    search_fields = ["id", ]

admin.site.register(Outfit, OutfitTypeAdmin)



class OutfitCalculationAdmin(admin.ModelAdmin):
    list_display = ("id", "outfit", "from_date", "to_date")
    list_display_links = ("id",)
    search_fields = ["id", ]

admin.site.register(OutfitCalculation, OutfitCalculationAdmin)


class FastContactAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "guid", 
        "full_name", 
        "phone_number", 
        )
    list_display_links = ('id' ,"guid",)

admin.site.register(FastContact, FastContactAdmin)