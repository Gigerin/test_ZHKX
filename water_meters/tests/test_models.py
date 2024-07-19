import pytest
from django.db.utils import IntegrityError
from decimal import Decimal
from django.utils import timezone

from buildings.models import Building
from water_meters.models import (
    WaterTariff,
    MaintenanceTariff,
    WaterMeter,
    MonthlyWaterUsage,
)
from apartments.models import (
    Apartment,
)  # Assuming this is where the Apartment model is defined


@pytest.mark.django_db
def test_create_water_tariff():
    tariff = WaterTariff.objects.create(
        name="Standard Tariff", price_per_unit=Decimal("1.50")
    )
    assert tariff.name == "Standard Tariff"
    assert tariff.price_per_unit == Decimal("1.50")


@pytest.mark.django_db
def test_create_maintenance_tariff():
    tariff = MaintenanceTariff.objects.create(
        name="Basic Maintenance", price_per_unit=Decimal("2.00")
    )
    assert tariff.name == "Basic Maintenance"
    assert tariff.price_per_unit == Decimal("2.00")


@pytest.mark.django_db
def test_create_water_meter(apartment):
    water_meter = WaterMeter.objects.create(
        apartment=apartment, name="Meter 1", reading=Decimal("123.45")
    )
    assert water_meter.name == "Meter 1"
    assert water_meter.reading == Decimal("123.45")
    assert water_meter.apartment == apartment


@pytest.mark.django_db
def test_create_monthly_water_usage(water_meter):
    date = timezone.now().date()
    apartment = water_meter.apartment
    usage = MonthlyWaterUsage.objects.create(
        water_meter=water_meter,
        apartment=apartment,
        date=date,
        water_used=Decimal("10.75"),
    )
    assert usage.water_meter == water_meter
    assert usage.date == date
    assert usage.water_used == Decimal("10.75")


@pytest.fixture
def building(db):
    return Building.objects.create(name="Building 1", address="123 Main St")


@pytest.fixture
def water_meter(db):
    return WaterMeter.objects.create(name="Building 1", address="123 Main St")


@pytest.fixture
def water_tariff(db):
    return WaterTariff.objects.create(name="Standard", price_per_unit=Decimal("50.5"))


@pytest.fixture
def maintenance_tariff(db):
    return MaintenanceTariff.objects.create(
        name="Standard", price_per_unit=Decimal("102.2")
    )


@pytest.fixture
def apartment(db, building, water_tariff, maintenance_tariff):
    return Apartment.objects.create(
        number="Apartment 1",
        building=building,
        area_sq_m=50,
        water_tariff=water_tariff,
        maintenance_tariff=maintenance_tariff,
    )


@pytest.fixture
def water_meter(apartment, db):
    return WaterMeter.objects.create(
        apartment=apartment, name="Meter 1", reading=Decimal("123.45")
    )
