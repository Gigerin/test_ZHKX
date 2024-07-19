from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from water_meters.models import WaterMeter
from water_meters.serializers import WaterMeterSerializer
from .models import Building, Apartment
from .serializers import ApartmentSerializer

@api_view(['GET'])
def get_water_meters_for_apartment(request, apartment_id):
    apartment = get_object_or_404(Apartment, pk=apartment_id)
    water_meters = WaterMeter.objects.filter(apartment=apartment)
    serializer = WaterMeterSerializer(water_meters, many=True)
    return Response({'apartment_id': apartment.pk, 'water_meters': serializer.data})