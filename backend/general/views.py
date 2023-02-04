from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status, permissions
from .models import Interview
from general.serializers import InterviewSerializers, InterviewLiteSerializers


class InterviewAPIView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializers


class InterviewListAPIView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Interview.objects.all().order_by("-date")
    serializer_class = InterviewLiteSerializers
