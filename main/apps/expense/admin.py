from django.contrib import admin
from .models import OtherExpense


class OtherExpenseAdmin(admin.ModelAdmin):
    list_display = ("guid", "title", "amount")
    list_display_links = ("guid",)
    search_fields = ["id"]

admin.site.register(OtherExpense, OtherExpenseAdmin)

