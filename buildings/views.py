from decimal import Decimal

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Building, CalculationProgress
from apartments.models import Apartment
from apartments.serializers import ApartmentSerializer
from .serializers import BuildingSerializer, BuildingAddressSerializer
from apartments.tasks import calculate_rent_for_apartment


@api_view(["GET"])
def get_apartments_in_building(request, building_id):
    building = get_object_or_404(Building, id=building_id)
    apartments = Apartment.objects.filter(building=building)
    serializer = ApartmentSerializer(apartments, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_building_address(request, building_id):
    building = get_object_or_404(Building, id=building_id)
    data = {"id": building.id, "address": building.address}
    serializer = BuildingAddressSerializer(data)
    return Response(serializer.data)


@api_view(["POST"])
def calculate_rent_building(request, building_id, month, year):
    if not (1 <= month <= 12 and 2000 <= year <= 2025):
        return Response(
            {"error": "Invalid year or month."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    building = get_object_or_404(Building, id=building_id)
    apartments = Apartment.objects.filter(building=building)

    progress = CalculationProgress.objects.create(
        building=building,
        total_apartments=apartments.count(),
        completed_apartments=0,
        status="in_progress",
        total_rent=Decimal(0.0),
    )

    for apartment in apartments:
        calculate_rent_for_apartment.delay(apartment.pk, progress.id, month, year)

    return Response({"message": "Calculation started", "progress_id": progress.id})


@api_view(["GET"])
def check_calculation_progress(
    request, building_id, progress_id
):
    """
    Проверяет прогресс текущего вычисления
    :param request:
    :param building_id: номер здания в котором проводиться вычисление
    :param progress_id: ID вычисления
    :return: либо прогресс видо обработанные квартиры/все квартиры, либо результат, либо ошибку
    """
    progress = get_object_or_404(CalculationProgress, id=progress_id)
    return Response(
        {
            "building_id": progress.building.id,
            "total_apartments": progress.total_apartments,
            "completed_apartments": progress.completed_apartments,
            "status": progress.status,
            "total_rent": str(progress.total_rent),
        }
    )
