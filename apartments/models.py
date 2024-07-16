from django.db import models
from buildings.models import Building


# Create your models here.
class Apartment(models.Model):
    number = models.CharField(max_length=4, primary_key=True)
    apartment_complex = models.ForeignKey(Building, on_delete=models.CASCADE)
    area = models.DecimalField(max_digits=10, decimal_places=2)