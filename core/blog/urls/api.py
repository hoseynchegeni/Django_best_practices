from django.urls import path, include


urlpatterns = [
    path("api/v1/", include("blog.api.v1.urls"), name="api_v1"),
]
