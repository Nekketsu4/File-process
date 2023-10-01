from rest_framework import serializers

from .models import *


class FilesSerializer(serializers.ModelSerializer):

    processed = serializers.BooleanField(read_only=True)

    class Meta:
        model = File
        fields = '__all__'