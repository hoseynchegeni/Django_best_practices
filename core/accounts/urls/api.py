from django.urls import path, include

urlpatterns = [
    path("api/v1/", include("accounts.api.v1.urls"), name="accounts_api_v1"),
    path('api/v2/', include('djoser.urls')),
]
