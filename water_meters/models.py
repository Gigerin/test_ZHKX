from django.db import models
from django.utils import timezone



class WaterTariff(models.Model):
    name = models.CharField(max_length=255)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)


class MaintenanceTariff(models.Model):
    name = models.CharField(max_length=255)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)


class WaterMeter(models.Model):
    apartment = models.ForeignKey('apartments.Apartment', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    reading = models.DecimalField(max_digits=100, decimal_places=2)


class MonthlyWaterUsage(models.Model):
    apartment = models.ForeignKey('apartments.Apartment', on_delete=models.CASCADE)
    water_meter = models.ForeignKey(WaterMeter, on_delete=models.CASCADE)
    date = models.DateField()
    water_used = models.DecimalField(max_digits=10, decimal_places=2)  # Units of water used in the month
