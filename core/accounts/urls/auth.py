from django.urls import path, include
from ..views import send_email, test

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("send", send_email, name = 'send_email'),
    path('test/',test, name= 'test'),
    ]

