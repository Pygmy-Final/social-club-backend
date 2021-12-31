from .models import CustomUser, Follow
from rest_framework import serializers

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = "__all__"

class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = "__all__"


# class UserSerializer(serializers.ModelSerializer):
#     profile = UserProfileSerializer(required=True)

#     class Meta:
#         model = CustomUser
#         fields = ('id','username','email', 'first_name', 'last_name', 'password', 'profile')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         profile_data = validated_data.pop('profile')
#         password = validated_data.pop('password')
#         user = CustomUser(**validated_data)
#         user.set_password(password)
#         user.save()
#         Profile.objects.create(user=user, **profile_data)
#         return user

#     def update(self, instance, validated_data):
#         profile_data = validated_data.pop('profile')
#         profile = instance.profile

#         instance.email = validated_data.get('email', instance.email)
#         instance.save()

#         profile.user = profile_data.get('user', profile.user)
#         profile.gender = profile_data.get('bio', profile.bio)
#         profile.profilePicture = profile_data.get('dob', profile.dob)
#         profile.interests = profile_data.get('city', profile.city)
#         profile.save()

#         return instance