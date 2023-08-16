from django.urls import path
from ..views import calculation


urlpatterns = [
    path(
        'flightcalculation-list/',
        view=calculation.flightcalculation_list_api_view,
        name='flightcalculation_list'
    ),
    path(
        'flightcalculation-create/',
        view=calculation.flightcalculation_create_api_view,
        name='flightcalculation_create'
    ),
    path(
        'flightcalculation-data/',
        view=calculation.flight_calculation_analytics,
        name='flightcalculation_data'
    ),
    path(
        'single-flightcalculation-detail/<int:pk>/',
        view=calculation.single_flight_calculation_detail_api_view,
        name='single_flightcalculation_detail'
    ),
]