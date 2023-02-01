from django.urls import include, path

urlpatterns = [
    path("", include("accounts.urls.api")),
    path("", include("accounts.urls.post")),
]
