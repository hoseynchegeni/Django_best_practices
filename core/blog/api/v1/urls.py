from django.urls import path
from .views import PostList, PostDetail, PostViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

app_name = "api_v1"

router = DefaultRouter()
router.register("post", PostViewSet, basename="post")
router.register("category", CategoryViewSet, basename="category")
urlpatterns = router.urls

