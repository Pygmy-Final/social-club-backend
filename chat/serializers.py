from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

    def create(self, validated_data): #post
        user_id =self.context['request'].user.id
        validated_data['sender'].id=user_id
        return Message.objects.create(**validated_data) 