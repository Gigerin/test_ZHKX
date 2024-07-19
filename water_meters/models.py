from django.db import models
from django.utils import timezone


class WaterTariff(models.Model):
    name = models.CharField(max_length=255)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class MaintenanceTariff(models.Model):
    name = models.CharField(max_length=255)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class WaterMeter(models.Model):
    apartment = models.ForeignKey("apartments.Apartment", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    current_reading = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.apartment}"


class WaterMeterReading(models.Model):
    water_meter = models.ForeignKey(
        WaterMeter, on_delete=models.CASCADE, related_name="readings"
    )
    reading = models.DecimalField(max_digits=100, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.date} - {self.reading}"
