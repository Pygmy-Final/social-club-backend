from .models import CustomUser, Follow
from .serializers import FollowSerializer, UserProfileSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .permissions import UserWritePermiss, IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.filters import SearchFilter
from django.db.models import Q

class UserProfileListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends= [SearchFilter]
    search_fields = ['interests']

    # def  get_queryset(self, *args, **kwargs):
    #     user_id = str(self.request.user) 
    #     queryset = CustomUser.objects.exclude(id = user_id)
    #     return queryset

class UserProfileCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all() 
    serializer_class = UserProfileSerializer
    permission_classes = (AllowAny,)
  
class UserInfoView(generics.ListAPIView, UserWritePermiss):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (UserWritePermiss,)
    filter_backends= [SearchFilter]
    search_fields = ['username']

class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView, UserWritePermiss):
    queryset = CustomUser.objects.all() 
    serializer_class = UserProfileSerializer
    permission_classes = (UserWritePermiss,)


class FollowListView(generics.ListAPIView):
    # queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends= [SearchFilter]
    search_fields = ['from_user']

    def  get_queryset(self, *args, **kwargs):
        user_id = str(self.request.user) 
        queryset = Follow.objects.filter(from_user = user_id)
        return queryset

class FollowCreateView(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)