from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/users/register', views.registration_api_view),
    path('api/v1/users/authorize', views.authorization_api_view),
    path('api/v1/users/confirm', views.confirmation_api_view),
]