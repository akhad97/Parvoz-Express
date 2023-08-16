from django.contrib import admin
from .models import (
    Client, 
    Partner,
    VisaClient
)


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "guid", 
        "full_name", 
        "dob", 
        "room_type", 
        "total_amount", 
        "remained_amount"
        )
    list_display_links = ("guid",)
    search_fields = ["id", "full_name"]

admin.site.register(Client, ClientAdmin)


class VisaClientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        "guid", 
        "visa", 
        "hotel", 
        "full_name"
        )
    list_display_links = ("guid",)
    search_fields = ["id", "full_name"]

admin.site.register(VisaClient, VisaClientAdmin)


class PartnerAdmin(admin.ModelAdmin):
    list_display = (
        "guid", 
        "full_name", 
        "dob", 
        "total_amount", 
        "remained_amount"
        )
    list_display_links = ("guid",)
    search_fields = ["id", "full_name"]

admin.site.register(Partner, PartnerAdmin)