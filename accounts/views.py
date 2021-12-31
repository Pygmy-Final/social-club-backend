from django.shortcuts import render
from .models import CustomUser, Follow
from .serializers import FollowSerializer, UserProfileSerializer
from rest_framework import generics
# from .permissions import EventUserWritePermiss
from rest_framework.permissions import IsAuthenticated


class UserProfileListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)


class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)



# follow has views ***********