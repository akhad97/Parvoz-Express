from django.urls import path
from . import views



urlpatterns = [
    path(
        '<uuid:guid>/client-list/',
        view=views.client_list_api_view,
        name='client_list'
    ),
    path(
        'client-create/',
        view=views.client_create_api_view,
        name='client_create'
    ),
    path(
        '<uuid:guid>/client-detail/',
        view=views.client_detail_api_view,
        name='client_detail'
    ),
    path(
        '<uuid:guid>/client-update/',
        view=views.client_update_api_view,
        name='client_update'
    ),
    path(
        '<uuid:guid>/partner-list/',
        view=views.partner_list_api_view,
        name='partner_list'
    ),
    path(
        'partner-create/',
        view=views.partner_create_api_view,
        name='partner_create'
    ),
    path(
        '<uuid:guid>/partner-update/',
        view=views.partner_update_api_view,
        name='partner_update'
    ),
    path(
        '<int:pk>/visaclient-list/',
        view=views.visa_client_list_api_view,
        name='visa_client_list'
    ),
    path(
        'visaclient-create/',
        view=views.visa_client_create_api_view,
        name='visa_client_create'
    ),
    path(
        '<uuid:guid>/visaclient-update/',
        view=views.visa_client_update_api_view,
        name='visa_client_update'
    ),
]
