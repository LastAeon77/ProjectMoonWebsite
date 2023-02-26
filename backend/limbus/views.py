from .models import Sinner, Identity, EGO
from .serializers import IdentitySerializers, EGOSerializers
from rest_framework import generics, permissions


class IdentitySerial(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Identity.objects.all()
    serializer_class = IdentitySerializers


class EGOSerial(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = EGO.objects.all()
    serializer_class = EGOSerializers
