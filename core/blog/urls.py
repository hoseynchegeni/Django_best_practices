from django.urls import path
from django.views.generic import TemplateView
from .views import indexView
urlpatterns = [
    path('', indexView.as_view()),
]