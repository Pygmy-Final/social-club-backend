from .models import CustomUser, Follow
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','email','password','gender','phonenumber','profilePicture','interests')

class FollowSerializer(serializers.ModelSerializer):

    def create(self, validated_data): #post
        user_id =self.context['request'].user.id
        validated_data['from_user'].id=user_id
        return Follow.objects.create(**validated_data)  
        
    class Meta:
        model = Follow
        fields = "__all__"
