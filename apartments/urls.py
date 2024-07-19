# urls.py
from django.urls import path

from apartments.views import get_water_meters_for_apartment

urlpatterns = [
    path(
        "<str:apartment_id>/water_meters/",
        get_water_meters_for_apartment,
        name="get_water_meters_for_apartment",
    ),
]
