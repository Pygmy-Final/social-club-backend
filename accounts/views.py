from django.shortcuts import render
from .models import CustomUser, Follow
from .serializers import FollowSerializer, UserProfileSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views import View
from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from django.core.serializers import serialize
import json

class UserProfileListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        user_id= request.user
        current_inter=''
        queryset = CustomUser.objects.all()
        for q in queryset:
            if str(q.id) == str(user_id):
                current_inter = q.interests
        current_inter = list(current_inter)
        dec_pepole = {k: [] for k in current_inter}

        pepole_list=[]
        for q in queryset:
            if str(q.id) != str(user_id) and q.interests :
                for int in current_inter:
                    if int in q.interests:
                        # print('*'*50, json.dumps(q ,indent=4,))
                        # dec_pepole[int].append(q)
                        # serializer = serializer+UserProfileSerializer(q)
                        pepole_list.append(q)
                        break
        # serializer_class = UserProfileSerializer(pepole_list[0])
        data = []
        # queryset = CustomUser.objects.get()
        for item in pepole_list:
            serializer_class = UserProfileSerializer(item)
            data.append(serializer_class.data)
        print('*'*50, data)
        # return Response(serializers.serialize('json',pepole_list) )
        return Response(serializer_class.data)


class UserProfileCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (AllowAny,)

class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)



# follow has views ***********

class FollowListView(generics.RetrieveAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)