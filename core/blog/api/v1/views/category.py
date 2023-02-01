from ..serializers import CategorySerializer
from ....models import Category
from rest_framework import viewsets

from rest_framework.permissions import (
    IsAuthenticated,
)


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
