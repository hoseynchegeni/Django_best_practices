from django.urls import include, path

urlpatterns = [
    path("", include("blog.api.v1.urls.post")),
    path("", include("blog.api.v1.urls.category")),
]
