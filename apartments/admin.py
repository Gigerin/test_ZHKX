from django.contrib import admin
from .models import Apartment

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ("number", "building", "area_sq_m")
    list_filter = ("number",)
    search_fields = ("number", "building", "area_sq_m")


