from django.urls import path
from django.views.generic import TemplateView, RedirectView
from .views import indexView, RedirectToGoogle, PostList, PostDetailView,PostCreate, PostEditView
app_name = 'blog'


urlpatterns = [
    path('', indexView.as_view(), name  = 'ClassBasedView'),
    path('google', RedirectView.as_view( url = 'https://google.com/')),
    path('class_based_view', RedirectView.as_view(pattern_name = 'blog:ClassBasedView')),
    path('google_redirect',RedirectToGoogle.as_view()),
    path('post/',PostList.as_view(), name= 'PostList'),
    path('post/<int:pk>/',PostDetailView.as_view(), name = 'PostDetail'),
    path('create/',PostCreate.as_view(), name= 'create'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name= 'edit'),
]