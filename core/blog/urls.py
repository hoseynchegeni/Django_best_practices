from django.urls import path, include
from django.views.generic import RedirectView
from .views import (
    indexView,
    PostList,
    PostDetailView,
    PostCreate,
    PostEditView,
    PostDeleteView,
    PostListAPiView
)

app_name = "post"

urlpatterns = [
    path("", indexView.as_view(), name="ClassBasedView"),
    path(
        "class_based_view",
        RedirectView.as_view(pattern_name="blog:ClassBasedView"),
    ),
    path("post/", PostList.as_view(), name="PostList"),
    path("post/api/", PostListAPiView.as_view(), name="PostListApi"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="PostDetail"),
    path("create/", PostCreate.as_view(), name="create"),
    path("post/<int:pk>/edit/", PostEditView.as_view(), name="edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="delete"),
    path("api/v1/", include("blog.api.v1.urls"), name="api_v1"),
]
