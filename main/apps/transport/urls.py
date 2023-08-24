from django.urls import path
from . import views



urlpatterns = [
    path(
        'transport-list/',
        view=views.transport_list_api_view,
        name='transport_list'
    ),
    path(
        'transport-create/',
        view=views.transport_create_api_view,
        name='transport_create'
    ),
    path(
        'transportcalculation-list/',
        view=views.transportcalculation_list_api_view,
        name='transportcalculation_list'
    ),
    path(
        'single-transportcalculation-detail/<int:pk>/',
        view=views.single_transport_calculation_detail_api_view,
        name='transportcalculation_detail'
    ),
    path(
        'transportcalculation-create/',
        view=views.transportcalculation_create_api_view,
        name='transportcalculation_create'
    ),
    path(
        '<uuid:guid>/transportcalculation-delete/',
        view=views.transportcalculation_delete_api_view,
        name='transportcalculation-delete'
    ),
    path(
        'transport-update/<uuid:guid>/',
        view=views.transport_detail_api_view,
        name='transport-update'
    ),
    path(
        'transport-delete/<uuid:guid>/',
        view=views.transport_delete_api_view,
        name='transport-delete'
    ),
    path(
        'transporttype-data/',
        view=views.transport_type_percentage_api_view,        
        name='transporttype_data'
    ),
    path(
        'transportcalculation-data/',
        view=views.transport_calculation_analytics,        
        name='transporcalculation_data'
    ),
    
    
]