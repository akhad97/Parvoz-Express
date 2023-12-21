from django.contrib import admin
from .models import User, Region, AgentCalculation


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "guid", 
        "phone_number", 
        "full_name", 
        "email"
        )
    list_display_links = ('id' ,"guid",)
    search_fields = ["full_name", ]

admin.site.register(User, UserAdmin)
admin.site.register(Region)
admin.site.register(AgentCalculation)