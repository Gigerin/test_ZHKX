from django.contrib import admin
from .models import WaterTariff, MaintenanceTariff, WaterMeter, MonthlyWaterUsage

@admin.register(WaterTariff)
class WaterTariffAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_unit')
    search_fields = ('name',)


@admin.register(MaintenanceTariff)
class MaintenanceTariffAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_unit')
    search_fields = ('name',)


@admin.register(WaterMeter)
class WaterMeterAdmin(admin.ModelAdmin):
    list_display = ('apartment', 'name', 'reading')
    search_fields = ('name', 'apartment__name')  # Assuming apartment has a name field


@admin.register(MonthlyWaterUsage)
class MonthlyWaterUsageAdmin(admin.ModelAdmin):
    list_display = ('apartment', 'water_meter', 'date', 'water_used')
    list_filter = ('date',)
    search_fields = ('apartment__name', 'water_meter__name')  # Assuming apartment and water meter have name fields
