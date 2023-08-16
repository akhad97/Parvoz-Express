from django.urls import path
from ..views import flight


urlpatterns = [
    path(
        'flight-landing-search/',
        view=flight.flight_landing_serach_api_view,
        name='flight_landing_search'
    ),
    path(
        'flighttype-list/',
        view=flight.flight_type_list_api_view,
        name='flight_type_list'
    ),
    path(
        'flight-list/',
        view=flight.flight_list_api_view,
        name='flight_list'
    ),
    path(
        'flight-create/',
        view=flight.flight_create_api_view,
        name='flight_create'
    ),
    path(
        '<uuid:guid>/flight-detail/',
        view=flight.flight_detail_list_api_view,
        name='flight_detial'
    ),
    path(
        '<uuid:guid>/flight-update/',
        view=flight.flight_update_list_api_view,
        name='flight_update'
    ),
    path(
        'flightbook-create/',
        view=flight.flight_book_create_api_view,
        name='flight_book_create'
    ),
    path(
        'flightbook-list/',
        view=flight.flight_book_list_api_view,
        name='flight_book_list'
    ),
    path(
        '<uuid:guid>/flightbook-update/',
        view=flight.flight_book_update_api_view,
        name='flight_book_update'
    ),
]