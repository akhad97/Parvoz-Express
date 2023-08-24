from django.urls import path
from . import views


urlpatterns = [
    path(
        'register/', 
        views.user_registration_api_view, 
        name='register'
    ),
    path(
        'login/', 
        views.user_login_api_view, 
        name='login'
    ),
    path(
        'list/', 
        views.user_list_api_view, 
        name='list'
    ),
    path(
        '<uuid:guid>/detail/', 
        views.user_detail_api_view, 
        name='detail'
    ),
    path(
        '<uuid:guid>/update/', 
        views.user_update_delete_api_view, 
        name='update'
    ),
    path(
        'region-list/', 
        views.region_list_api_view, 
        name='region_list'
    ),
    path(
        "password-change/", 
        view=views.password_change_api_view, 
        name="password_change"
    )
]
