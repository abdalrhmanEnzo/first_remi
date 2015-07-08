from remi_app.models import User
from rest_framework import viewsets
import remi_app.serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = remi_app.serializers.UserSerializer
