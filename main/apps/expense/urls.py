from django.urls import path
from . import views



urlpatterns = [
    path(
        'tourpackage-otherexpense-create/',
        view=views.tourpackage_otherexpense_create_api_view,
        name='tourpackage_otherexpense_create'
    ),
    path(
        'otherexpense-list/',
        view=views.otherexpense_list_api_view,
        name='otherexpense_list'
    ),
    path(
        'otherexpense-create/',
        view=views.otherexpense_create_api_view,
        name='otherexpense_create'
    ),
    path(
        'otherexpense-data/',
        view=views.otherexpense_view_data_api_view,
        name='otherexpense_data'
    ),
    path(
        'otherexpense-update/<uuid:guid>/',
        view=views.otherexpense_update_api_view,
        name='otherexpense_update'
    )
]