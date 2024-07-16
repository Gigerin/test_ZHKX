from django.contrib import admin

from buildings.models import Building


# Register your models here.
@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    list_filter = ("name",)
    search_fields = ("name",)