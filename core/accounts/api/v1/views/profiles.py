from rest_framework.generics import RetrieveUpdateAPIView

from ..serializers import ProfileSerializer
from django.contrib.auth import get_user_model
from ....models import Profile
from django.shortcuts import get_object_or_404


User = get_user_model()


class ProfileApiView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user.id)
        return obj
