from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Event


class EventSerialzer(serializers.ModelSerializer):
    class Meta:
        fields = ['EventName','EventDescription','EventLocation','EventCategory','EventStartTime','EventCreator','EventParticipants']
        model = Event