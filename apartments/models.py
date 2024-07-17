from django.db import models
from buildings.models import Building
from water_meters.models import WaterTariff, MaintenanceTariff


# Create your models here.
class Apartment(models.Model):
    number = models.CharField(max_length=4, primary_key=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    area_sq_m = models.DecimalField(max_digits=10, decimal_places=2)
    water_tariff = models.ForeignKey(WaterTariff, on_delete=models.CASCADE)
    maintenance_tariff = models.ForeignKey(MaintenanceTariff, on_delete=models.CASCADE)


    def __str__(self):
        return self.number