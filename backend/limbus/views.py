from .models import Sinner, Identity, EGO, Passive, PassiveEgo, Skill, SkillEgo
from .serializers import (
    IdentitySerializers,
    EGOSerializers,
    SkillSerializers,
    SkillEgoSerializers,
    PassiveSerializers,
    PassiveEgoSerializers,
)
from rest_framework import generics, permissions


class SkillSerial(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Skill.objects.all()
    serializer_class = SkillSerializers


class SkillEgoSerial(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = SkillEgo.objects.all()
    serializer_class = SkillEgoSerializers


class PassiveSerial(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Passive.objects.all()
    serializer_class = PassiveSerializers


class PassiveEgoSerial(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = PassiveEgo.objects.all()
    serializer_class = PassiveEgoSerializers


class IdentitySerial(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Identity.objects.all()
    serializer_class = IdentitySerializers


class EGOSerial(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = EGO.objects.all()
    serializer_class = EGOSerializers
