from django.urls import path, include
from .views import RegistrationApiView, CustomAuthToken,CustomDiscardAuthToken



app_name = 'api-v1'

urlpatterns = [
    path('registration/', RegistrationApiView.as_view(), name='register'),
    path('token/login/', CustomAuthToken.as_view(), name='token-login'),
    path('token/logout/', CustomDiscardAuthToken.as_view(), name= 'token-discard')
]