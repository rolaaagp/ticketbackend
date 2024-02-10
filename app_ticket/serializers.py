from rest_framework import serializers
from app_auth.serializers import UserSerializer
from . import models


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    manager = UserSerializer(read_only=True)
    status = StatusSerializer(read_only=True)

    class Meta:
        model = models.Ticket
        fields = '__all__'
