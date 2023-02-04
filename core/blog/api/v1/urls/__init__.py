from django.urls import include, path

app_name = 'api_v1'

urlpatterns = [
    path("", include("blog.api.v1.urls.post")),
    path("", include("blog.api.v1.urls.category")),
]
