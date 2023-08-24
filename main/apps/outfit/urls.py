from django.urls import path
from . import views



urlpatterns = [
    path(
        'outfit-list/',
        view=views.outfit_list_api_view,
        name='outfit_list'
    ),
    path(
        'outfit-create/',
        view=views.outfit_create_api_view,
        name='outfit_create'
    ),
    path(
        'outfit-update/<int:pk>/',
        view=views.outfit_detail_api_view,
        name='outfit_detail'
    ),
    path(
        'outfittype-list/',
        view=views.outfittype_list_api_view,
        name='outfittype_list'
    ),
    path(
        'outfittype-create/',
        view=views.outfittype_create_api_view,
        name='outfittype_create'
    ),
    path(
        'outfitcalculation-create/',
        view=views.outfit_calculation_create_api_view,
        name='outfitcalculation_create'
    ),
    path(
        'outfitcalculation-list/',
        view=views.outfit_calculation_list_api_view,
        name='outfitcalculation_list'
    ),
    path(
        '<uuid:guid>/outfitcalculation-delete/',
        view=views.outfit_calculation_delete_api_view,
        name='outfit_calculation_delete'
    ),
    path(
        'single-outfitcalculation-detail/<int:pk>/',
        view=views.single_outfit_calculation_detail_api_view,
        name='outfitcalculation_detail'
    ),
    path(
        'outfitcalculation-data/',
        view=views.outfitcalculation_analytics,
        name='outfitcalculation_data'
    ),
]
