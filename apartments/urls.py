# urls.py
from django.urls import path
from .views import get_apartments_in_building

urlpatterns = [
    path('buildings/<int:building_id>/apartments/', get_apartments_in_building, name='get_apartments_in_building'),
]
