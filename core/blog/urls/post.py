from django.urls import path
from django.views.generic import RedirectView
from ..views import (
    indexView,
    PostList,
    PostDetailView,
    PostCreate,
    PostEditView,
    PostDeleteView,
)

app_name = "post"

urlpatterns = [
    path("", indexView.as_view(), name="ClassBasedView"),
    path(
        "class_based_view",
        RedirectView.as_view(pattern_name="blog:ClassBasedView"),
    ),
    path("post/", PostList.as_view(), name="PostList"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="PostDetail"),
    path("create/", PostCreate.as_view(), name="create"),
    path("post/<int:pk>/edit/", PostEditView.as_view(), name="edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="delete"),
]
