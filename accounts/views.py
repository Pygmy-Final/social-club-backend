from .models import CustomUser, Follow
from .serializers import FollowSerializer, UserProfileSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .permissions import UserWritePermiss, IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.filters import SearchFilter
from django.db.models import Q
class UserProfileListView(generics.ListAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends= [SearchFilter]
    search_fields = ['interests']

    def  get_queryset(self, *args, **kwargs):
        user_id = str(self.request.user) 
        queryset = CustomUser.objects.exclude(id = user_id)
        return queryset

class UserProfileCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all() 
    serializer_class = UserProfileSerializer
    permission_classes = (AllowAny,)
    # def get_permissions(self):
    #     permission_classes = []
    #     if self.action == 'create':
    #         permission_classes = [AllowAny]
    #     elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
    #         permission_classes = [IsLoggedInUserOrAdmin]
    #     elif self.action == 'list' or self.action == 'destroy':
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]

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