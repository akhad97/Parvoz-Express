from django.urls import path
from . import views



urlpatterns = [
    path(
        'visa-list/',
        view=views.visa_list_api_view,
        name='visa_list'
    ),
    path(
        'visa-detail/<int:pk>/',
        view=views.visa_detail_api_view,
        name='visa_detail'
    ),
    path(
        'visa-create/',
        view=views.visa_create_api_view,
        name='visa_create'
    ),
    path(
        '<uuid:guid>/visa-delete/',
        view=views.visa_delete_api_view,
        name='visa_delete'
    ),
    path(
        'visacalculation-list/',
        view=views.visacalculation_list_api_view,
        name='visacalculation_list'
    ),
    path(
        'visacalculation-create/',
        view=views.visacalculation_create_api_view,
        name='visacalculation_create'
    ),
    path(
        '<uuid:guid>/visacalculation-delete/',
        view=views.visacalculation_delete_api_view,
        name='visacalculation_delete'
    ),
    path(
        'single-visacalculation-detail/<int:pk>/',
        view=views.single_visa_calculation_detail_api_view,
        name='single_visa_calculation_detail'
    ),
    path(
        'visabook-create/',
        view=views.visabook_create_api_view,
        name='visabook_create'
    ),
    path(
        'visabook-list/',
        view=views.visabook_list_api_view,
        name='visabook_list'
    ),
    path(
        '<uuid:guid>/visabook-update/',
        view=views.visa_book_update_api_view,
        name='visabook_update'
    )
]