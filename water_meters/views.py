import datetime
from decimal import Decimal

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from water_meters.models import WaterMeter, WaterMeterReading
from water_meters.serializers import WaterMeterReadingSerializer
from water_meters.utils import convert_string_date_to_datetime


# Create your views here.


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def submit_reading(request, water_meter_id):
    """
    Арендует велосипед по pk
    :param request:
    :param pk: ID велосипеда
    :return: данные об успешно арендованном велосипеде
    """
    try:
        water_meter = WaterMeter.objects.get(pk=water_meter_id)
    except WaterMeter.DoesNotExist:
        return Response(
            {"error": "Счетчик не найден."}, status=status.HTTP_404_NOT_FOUND
        )

    data = request.data.copy()
    data["water_meter"] = water_meter_id
    water_meter_reading_serializer = WaterMeterReadingSerializer(data=data)
    if water_meter_reading_serializer.is_valid():
        try:

            date = convert_string_date_to_datetime(data["date"])
            print(date)
            reading = WaterMeterReading.objects.get(pk=water_meter_id, date=date)
            reading.water_meter = Decimal(data["reading"])
            return Response(
                water_meter_reading_serializer.data, status=status.HTTP_200_OK
            )
        except WaterMeterReading.DoesNotExist:
            water_meter_reading_serializer.save()
    else:
        return Response(
            water_meter_reading_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
    return Response(water_meter_reading_serializer.data, status=status.HTTP_200_OK)
