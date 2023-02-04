from rest_framework import serializers
from general.models import Interview


class InterviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ["id", "name", "body", "date", "last_modified"]


class InterviewLiteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ["id", "name", "date", "last_modified"]
