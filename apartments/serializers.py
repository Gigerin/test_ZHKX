# serializers.py
from rest_framework import serializers
from .models import Apartment

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ['number', 'building', 'area_sq_m']
