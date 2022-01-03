from .models import CustomUser, Follow
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','email','password','gender','phonenumber','profilePicture','interests')
    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

class FollowSerializer(serializers.ModelSerializer):

    def create(self, validated_data): #post
        user_id =self.context['request'].user.id
        validated_data['from_user'].id=user_id
        return Follow.objects.create(**validated_data)  
        
    class Meta:
        model = Follow
        fields = "__all__"


from django.contrib.auth.hashers import make_password

