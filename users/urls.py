from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/users/register', views.RegistrationAPIView.as_view()),
    path('api/v1/users/authorize', views.AuthorizationAPIView.as_view()),
    path('api/v1/users/confirm', views.ConfirmationAPIView.as_view()),
]