from django.contrib import admin
from .models import WaterTariff, MaintenanceTariff, WaterMeter, WaterMeterReading


@admin.register(WaterTariff)
class WaterTariffAdmin(admin.ModelAdmin):
    list_display = ("name", "price_per_unit")
    search_fields = ("name",)


@admin.register(MaintenanceTariff)
class MaintenanceTariffAdmin(admin.ModelAdmin):
    list_display = ("name", "price_per_unit")
    search_fields = ("name",)


@admin.register(WaterMeter)
class WaterMeterAdmin(admin.ModelAdmin):
    list_display = ("apartment", "name")
    search_fields = ("name", "apartment__number")


@admin.register(WaterMeterReading)
class WaterMeterReadingAdmin(admin.ModelAdmin):
    list_display = ("water_meter", "reading", "date")
    search_fields = ("water_meter__name", "water_meter__apartment__number")
    list_filter = ("date",)
