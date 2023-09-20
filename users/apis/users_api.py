from rest_framework import viewsets

from users.models import UserModel
from users.serializer import UserModelsSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserModelsSerializer
    queryset = UserModel.objects.all()
