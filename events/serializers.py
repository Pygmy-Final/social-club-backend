from rest_framework import serializers
from .models import Event



class EventSerialzer(serializers.ModelSerializer):
   
    class Meta:
        fields = "__all__"
        model = Event

    

