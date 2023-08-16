from django.contrib import admin
from .models import (
    Manager, 
    Guide,
    ManagerCalculation,
    GuideCalculation
)


class ManagerAdmin(admin.ModelAdmin):
    list_display = ("id", "guid", "full_name", "nickname", "city")
    list_display_links = ("guid",)
    search_fields = ["full_name", ]

admin.site.register(Manager, ManagerAdmin)

class ManagerCalculationAdmin(admin.ModelAdmin):
    list_display = ("id", "guid", "manager")
    list_display_links = ("guid",)

admin.site.register(ManagerCalculation, ManagerCalculationAdmin)

class GuideAdmin(admin.ModelAdmin):
    list_display = ("id", "guid", "full_name", "nickname", "city")
    list_display_links = ("guid",)
    search_fields = ["full_name", ]

admin.site.register(Guide, GuideAdmin)

class GuideCalculationAdmin(admin.ModelAdmin):
    list_display = ("id", "guid", "guide")
    list_display_links = ("guid",)
    
admin.site.register(GuideCalculation, GuideCalculationAdmin)



