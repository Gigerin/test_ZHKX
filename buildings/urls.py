# urls.py
from django.urls import path
from apartments.views import get_apartments_in_building

urlpatterns = [
    path('<int:building_id>/apartments/', get_apartments_in_building, name='get_apartments_in_building'),
]
