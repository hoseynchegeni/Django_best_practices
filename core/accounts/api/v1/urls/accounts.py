from django.urls import path
from ..views import (
    RegistrationApiView,
    CustomAuthToken,
    CustomDiscardAuthToken,
    ChangePasswordView,
    TestSendMail,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("registration/", RegistrationApiView.as_view(), name="register"),
    path('test-email/', TestSendMail.as_view(),name= 'test-email'),
    path("token/login/", CustomAuthToken.as_view(), name="token-login"),
    path(
        "token/logout/",
        CustomDiscardAuthToken.as_view(),
        name="token-discard",
    ),
    path(
        "change-password/",
        ChangePasswordView.as_view(),
        name="change-password",
    ),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
]
