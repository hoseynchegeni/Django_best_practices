from django.urls import path, include
from .views import RegistrationApiView
from rest_framework.authtoken.views import ObtainAuthToken


app_name = 'api-v1'

urlpatterns = [
    path('registration/', RegistrationApiView.as_view(), name='register'),
    path('token/login/', ObtainAuthToken.as_view(), name='token-login'),
]