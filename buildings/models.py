from django.db import models

# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=255)