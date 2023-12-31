from django.urls import path
from . import views



urlpatterns = [
    path(
        'manager-list/',
        view=views.manager_list_api_view,
        name='manager_list'
    ),
    path(
        'manager-create/',
        view=views.manager_create_api_view,
        name='manager_create'
    ),
    path(
        '<uuid:guid>/manager-detail/',
        view=views.manager_detail_api_view,
        name='manager_detail'
    ),
    path(
        '<uuid:guid>/manager-delete/',
        view=views.manager_delete_api_view,
        name='manager_delete'
    ),
    path(
        '<uuid:guid>/manager-update/',
        view=views.manager_update_api_view,
        name='manager_update'
    ),
    path(
        'managercalculation-list/',
        view=views.managercalculation_list_api_view,
        name='managercalculation_list'
    ),
    path(
        'managercalculation-create/',
        view=views.managercalculation_create_api_view,
        name='managercalculation_create'
    ),
    path(
        '<int:pk>/managercalculation-detail/',
        view=views.managercalculation_detail_api_view,
        name='managercalculation_detail'
    ),
    path(
        '<int:pk>/managercalculation-update/',
        view=views.managercalculation_update_api_view,
        name='managercalculation_update'
    ),
    path(
        '<int:pk>/guide-list/',
        view=views.manager_guide_list_api_view,
        name='guide_list'
    ),
    path(
        'manager-login/',
        view=views.manager_login_api_view,
        name='manager_login'
    ),
    path(
        'guide-login/',
        view=views.guide_login_api_view,
        name='guide_login'
    ),
    path(
        'guide-list/',
        view=views.guide_list_api_view,
        name='guide_list'
    ),
    path(
        'guide-create/',
        view=views.guide_create_api_view,
        name='guide_create'
    ),
    path(
        '<uuid:guid>/guide-detail/',
        view=views.guide_detail_api_view,
        name='guide_detail'
    ),
    path(
        '<uuid:guid>/guide-delete/',
        view=views.guide_delete_api_view,
        name='guide_delete'
    ),
    path(
        '<uuid:guid>/guide-update/',
        view=views.guide_update_api_view,
        name='guide_update'
    ),
    path(
        'guidecalculation-list/',
        view=views.guidecalculation_list_api_view,
        name='guidecalculation_list'
    ),
    path(
        'guidecalculation-create/',
        view=views.guidecalculation_create_api_view,
        name='guidecalculation_create'
    ),
    path(
        '<int:pk>/guidecalculation-detail/',
        view=views.guidecalculation_detail_api_view,
        name='guidecalculation_detail'
    ),
    path(
        '<int:pk>/guidecalculation-update/',
        view=views.guidecalculation_update_api_view,
        name='guidecalculation_update'
    ),
    path(
        'managercalculation-data/',
        view=views.managercalculation_data_api_view,
        name='managercalculation_data'
    ),
    path(
        'guidecalculation-data/',
        view=views.guidecalculation_data_api_view,
        name='guidecalculation_data'
    ),
]
