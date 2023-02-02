from rest_framework.generics import GenericAPIView
from ..serializers import (
    RegistrationSerializer,
    CustomAuthTokenSerializer,
    ChangePasswordSerializer,
    ActivationResendSerializer,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from mail_templated import send_mail, EmailMessage
from ..utils import EmailThread
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
import jwt 
from jwt.exceptions import ExpiredSignatureError,InvalidSignatureError
from django.conf import settings

User = get_user_model()


class RegistrationApiView(GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Send Activation mail
            email = serializer.validated_data["email"]
            data = {"email": email}
            user_obj = get_object_or_404(User, email=email)
            token = self.get_token_for_user(user_obj)
            email_obj = EmailMessage(
                "email/activation_email.tpl",
                {"token": token},
                "admin@admin.com",
                to=[email],
            )
            EmailThread(email_obj).start()

            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class CustomAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.pk, "email": user.email})


class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChangePasswordView(GenericAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong Password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(
                {"Detail": "Password changed successfully"},
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestSendMail(GenericAPIView):
    def get(self, request, *args, **kwargs):
        self.email = "hoseyn@admin.com"
        user_obj = get_object_or_404(User, email=self.email)
        token = self.get_token_for_user(user_obj)
        email_obj = EmailMessage(
            "email/hello.tpl", {"token": token}, "admin@admin.com", to=[self.email]
        )
        EmailThread(email_obj).start()
        return Response("Email sent")

    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class ActivationApiView(GenericAPIView):
    def get(self, request,token, *args, **kwargs):
        try:
            token  = jwt.decode(token,settings.SECRET_KEY, algorithms = ['HS256'])
            user_id = token.get('user_id')
        except ExpiredSignatureError:
            return Response ({'detail':'Token has been expired'}, status= status.HTTP_400_BAD_REQUEST)
        except InvalidSignatureError:
            return Response ({'detail':'Token is not valid'}, status= status.HTTP_400_BAD_REQUEST)
        user_obj = User.objects.get(pk = user_id)
        if user_obj.is_verified:
             return Response({'detail':'Your account has been already verified'})
        user_obj.is_verified = True
        user_obj.save()

        return Response({'detail':'Your account have been verified and activated successfully'})
    

class ActivationResendApiView(GenericAPIView):
    serializer_class = ActivationResendSerializer
    def post(self, request, *args, **kwargs):
            serializer =ActivationResendSerializer(data= request.data)
            if serializer.is_valid(raise_exception= True):
                user_obj = serializer.validate['user']
                token = self.get_token_for_user(user_obj)
                email_obj = EmailMessage("email/activation_email.tpl",{"token": token},"admin@admin.com",to=[user_obj.email],)
                EmailThread(email_obj).start()
                return Response({'Details':'User activation resend successfully'}, status= status.HTTP_200_OK)


    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
