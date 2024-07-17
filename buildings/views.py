from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Building
from apartments.models import Apartment
from apartments.serializers import ApartmentSerializer
from .serializers import BuildingSerializer, BuildingAddressSerializer


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