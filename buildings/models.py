from django.db import models
from django.db.models import F
# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CalculationProgress(models.Model):
    building = models.ForeignKey('Building', on_delete=models.CASCADE)
    total_apartments = models.IntegerField()
    completed_apartments = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='in_progress')
    total_rent = models.DecimalField(max_digits=10, decimal_places=2)


    def update_progress(self, rent):
        self.completed_apartments = F('completed_apartments') + 1
        self.total_rent = self.total_rent + rent
        self.save()
        self.refresh_from_db()
        if self.completed_apartments >= self.total_apartments:
            self.status = 'completed'
            self.save(update_fields=['status'])

    def __str__(self):
        return f"Progress for building {self.building.id}: {self.completed_apartments}/{self.total_apartments}"