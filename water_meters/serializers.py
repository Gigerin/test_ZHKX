from rest_framework import serializers
from .models import WaterMeter, WaterMeterReading

class WaterMeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterMeter
        fields = ['id', 'apartment', 'name', 'current_reading']

class WaterMeterReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterMeterReading
        fields = ['id', 'water_meter', 'reading', 'date']

    
