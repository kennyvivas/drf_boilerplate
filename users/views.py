from django.urls import path, include
from users.models import CustomUser as User
from rest_framework import routers, serializers, viewsets
from users.serializers import UserSerializer

# Create your views here.
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer