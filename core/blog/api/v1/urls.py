from django.urls import path
from .views import PostList, PostDetail
app_name = 'api-v1'


urlpatterns = [
    # path('post/', PostList, name='post-list'),
    # path('post/<int:id>/', postDetail, name='post-detail'),
    path('post/',PostList.as_view(), name='post_list'),
    path('post/<int:id>/', PostDetail.as_view(), name= 'post_detail'),
]