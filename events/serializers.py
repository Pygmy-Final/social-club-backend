from rest_framework import serializers
from .models import Event

class EventSerialzer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Event

    def create(self, validated_data): #post
        user_id =self.context['request'].user.id
        validated_data['EventCreator'].id=user_id
        return Event.objects.create(**validated_data)

    

