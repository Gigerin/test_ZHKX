import random

from celery import shared_task
import time

from django.db import transaction

from apartments.models import Apartment
from apartments.serializers import ApartmentSerializer
from apartments.utils import return_previous_date
from buildings.models import CalculationProgress
from users.models import User
from users.serializers import UserSerializer
from celery.utils.log import get_task_logger
from django.db.models import F

from water_meters.models import WaterMeter, WaterMeterReading

logger = get_task_logger(__name__)


@shared_task
def calculate_rent_for_apartment(apartment_id, progress_id, month, year):
    apartment = Apartment.objects.get(pk=apartment_id)
    try:
        water_meter = WaterMeter.objects.get(
            apartment=apartment,
        )
    except WaterMeter.DoesNotExist:
        progress = CalculationProgress.objects.get(id=progress_id)
        progress.status = "error"
        progress.save()
        return {"error": "Apartment without watermeter."}
    previous_date = return_previous_date(month, year)
    try:
        water_meter_reading1 = WaterMeterReading.objects.filter(
            water_meter=water_meter,
            date__year=previous_date[1],
            date__month=previous_date[0],
        ).latest("date")
        logger.info(water_meter_reading1)
        water_meter_reading2 = WaterMeterReading.objects.filter(
            water_meter=water_meter, date__year=year, date__month=month
        ).latest("date")
    except WaterMeterReading.DoesNotExist:
        progress = CalculationProgress.objects.get(id=progress_id)
        progress.status = "error"
        progress.save()
        return {"error": "No readings found."}

    water_spent = water_meter_reading2.reading - water_meter_reading1.reading
    maintenance_tariff = apartment.maintenance_tariff.price_per_unit
    water_tariff = apartment.water_tariff.price_per_unit
    area = apartment.area_sq_m
    logger.info(
        f"Apartment {apartment_id} has Water spent: {water_spent}, Maintenance tariff: {maintenance_tariff}, water tariff: {water_tariff}, area: {area}"
    )

    sleep_time = random.randint(3, 7)
    time.sleep(sleep_time)
    total_rent = (water_spent * water_tariff) + (area * maintenance_tariff)
    logger.info(f"Apartment {apartment} has {total_rent}.")
    with transaction.atomic():
        progress = CalculationProgress.objects.get(id=progress_id)
        progress.update_progress(total_rent)
    return total_rent
