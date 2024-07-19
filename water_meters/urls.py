# urls.py
from django.urls import path
from buildings.views import get_apartments_in_building, get_building_address
from water_meters.views import submit_reading

urlpatterns = [
    path("<int:water_meter_id>/submit_reading/", submit_reading, name="submit_reading"),
]
