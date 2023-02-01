from django.urls import path, include

urlpatterns = [
    path("api/v1/", include("accounts.api.v1.urls"), name="accounts_api_v1"),
]
