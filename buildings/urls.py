# urls.py
from django.urls import path
from buildings.views import (
    get_apartments_in_building,
    get_building_address,
    calculate_rent_building,
    check_calculation_progress,
)

urlpatterns = [
    path(
        "<int:building_id>/apartments/",
        get_apartments_in_building,
        name="get_apartments_in_building",
    ),
    path(
        "<int:building_id>/address/", get_building_address, name="get_building_address"
    ),
    path(
        "<int:building_id>/calculate_rent/<int:year>/<int:month>/",
        calculate_rent_building,
        name="calculate_rent_building",
    ),
    path(
        "<int:building_id>/check_progress/<int:progress_id>/",
        check_calculation_progress,
        name="check_calculation_progress",
    ),
]
