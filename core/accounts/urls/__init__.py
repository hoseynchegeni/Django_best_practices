from django.urls import include, path

urlpatterns = [
    path("", include("accounts.urls.auth")),
    path("profile/", include("accounts.urls.api")),
]
