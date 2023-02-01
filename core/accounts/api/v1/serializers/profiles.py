from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from ....models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = Profile
        fields = ("id", "first_name", "last_name", "image", "desc", "email")
