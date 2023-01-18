from django.urls import path
from .views import PostList, PostDetail, PostViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'

router = DefaultRouter()
router.register('post', PostViewSet, basename='post')
urlpatterns = router.urls





# urlpatterns = [
#     # path('post/', PostList, name='post-list'),
#     # path('post/<int:id>/', postDetail, name='post-detail'),
#     # path('post/',PostList.as_view(), name='post_list'),
#     # path('post/<int:id>/', PostDetail.as_view(), name= 'post_detail'),
#     path('post/', PostViewSet.as_view({'get':'list', 'post':'create'}), name = 'post'),
#     path('post/<int:pk>/', PostViewSet.as_view({'get':'retrieve','updated':'put','delete':'destroy',}), name = 'post_detail')
# ]