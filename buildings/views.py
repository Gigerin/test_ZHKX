from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Building
from apartments.models import Apartment
from apartments.serializers import ApartmentSerializer
from .serializers import BuildingSerializer, BuildingAddressSerializer
from apartments.tasks import calculate_monthly_rent


@api_view(['GET'])
def get_apartments_in_building(request, building_id):
    building = get_object_or_404(Building, id=building_id)
    apartments = Apartment.objects.filter(building=building)
    serializer = ApartmentSerializer(apartments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_building_address(request, building_id):
    building = get_object_or_404(Building, id=building_id)
    data = {'id': building.id, 'address': building.address}
    serializer = BuildingAddressSerializer(data)
    return Response(serializer.data)

@api_view(['GET'])
def calculate_rent_building(request, building_id, month, year):
    if not (1 <= month <= 12 and 2000 <= year <= 2025):
        return Response({"error": "Invalid year or month."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    building = get_object_or_404(Building, id=building_id)
    apartments = Apartment.objects.filter(building=building)
    result = []
    for apartment in apartments:
        apartment_serializer = ApartmentSerializer(apartment)
        calculate_monthly_rent.delay(apartment_serializer.data, month, year)
    return Response({'result': result})

