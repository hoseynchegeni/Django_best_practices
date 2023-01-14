from django.urls import path
from .views import postDetail
app_name = 'api-v1'


urlpatterns = [
    path('post/<int:id>/', postDetail, name='post-detail')
]