from django.urls import path, include
from .views import RegistrationApiView


app_name = 'api-v1'

urlpatterns = [
    path('registration/', RegistrationApiView.as_view(), name='register')
]