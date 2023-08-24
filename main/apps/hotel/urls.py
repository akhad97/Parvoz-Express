from django.urls import path
from . import views



urlpatterns = [
    path(
        'hotel-landing-search/',
        view=views.hotel_landing_serach_api_view,
        name='hotel_landing_search'
    ),
    path(
        'hotel-list/',
        view=views.hotel_list_api_view,
        name='hotel_list'
    ),
    path(
        'hotel-create/',
        view=views.hotel_create_api_view,
        name='hotel_create'
    ),
    path(
        'hotel-update/<uuid:guid>/',
        view=views.hotel_detail_api_view,
        name='hotel_detail'
    ),
    path(
        'hotelcalculation-list/',
        view=views.hotelcalculation_list_api_view,
        name='hotelcalculation_list'
    ),
    path(
        'hotelcalculation-create/',
        view=views.hotelcalculation_create_api_view,
        name='hotelcalculation_create'
    ),
    path(
        'hotelcalculation-data/',
        view=views.hotelcalculation_data_api_view,
        name='hotelcalculation_data'
    ),
    path(
        'single-hotelcalculation-detail/<int:pk>/',
        view=views.single_hotel_calculation_detail_api_view,
        name='hotelcalculation_detail'
    ),
    path(
        '<uuid:guid>/hotelcalculation-delete/',
        view=views.hotelcalculation_delete_api_view,
        name='hotelcalculation_delete'
    ),
    path(
        'hotelbook-create/',
        view=views.hotelbook_create_api_view,
        name='hotel_landing_create'
    ),
    path(
        'hotelbook-list/',
        view=views.hotelbook_list_api_view,
        name='hotel_landing_list'
    ),
    path(
        '<uuid:guid>/hotelbook-update/',
        view=views.hotel_book_update_api_view,
        name='hotelbook_update'
    ),
]
