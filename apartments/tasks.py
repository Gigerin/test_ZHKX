from celery import shared_task
import time

from apartments.models import Apartment
from apartments.serializers import ApartmentSerializer
from apartments.utils import return_previous_date
from users.models import User
from users.serializers import UserSerializer
from celery.utils.log import get_task_logger

from water_meters.models import WaterMeter, WaterMeterReading

logger = get_task_logger(__name__)

@shared_task
def calculate_monthly_rent(serialized_apartment, month, year):
    apartment = Apartment.objects.get(
        number=serialized_apartment['number'],
        building=serialized_apartment['building'],
        area_sq_m=serialized_apartment['area_sq_m']
    )
    try:
        water_meter = WaterMeter.objects.get(
            apartment=apartment,
        )
    except WaterMeter.DoesNotExist:
        return {"error": "Apartment without watermeter."}
    previous_date = return_previous_date(month, year)
    try:
        water_meter_reading1 = WaterMeterReading.objects.get(water_meter=water_meter, date__year=previous_date[1], date__month=previous_date[0])
        water_meter_reading2 = WaterMeterReading.objects.get(water_meter=water_meter, date__year=year, date__month=month)
    except WaterMeterReading.DoesNotExist:
        return {"error": "No readings found."}

    logger.info(f'Calculated monthly rent for {water_meter_reading1}')
    water_spent = water_meter_reading2.reading - water_meter_reading1.reading
    maintenance_tariff = apartment.maintenance_tariff.price_per_unit
    water_tariff = apartment.water_tariff.price_per_unit
    area = apartment.area_sq_m

    total_rent = (water_spent * water_tariff) + (area * maintenance_tariff)
    logger.info(f"Apartment {apartment} has {total_rent} with {water_spent} cubic meters of water spent.")
    return total_rent