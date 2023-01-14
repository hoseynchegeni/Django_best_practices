from django.urls import path
from .views import apiView
app_name = 'api-v1'


urlpatterns = [
    path('post/', apiView, name='post-list')
]