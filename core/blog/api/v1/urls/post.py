from ..views import  PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("post", PostViewSet, basename="post")
urlpatterns = router.urls
