from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Building, Apartment
from .serializers import ApartmentSerializer

@api_view(['GET'])
def get_apartments_in_building(request, building_id):
    building = get_object_or_404(Building, id=building_id)
    apartments = Apartment.objects.filter(building=building)
    serializer = ApartmentSerializer(apartments, many=True)
    return Response(serializer.data)