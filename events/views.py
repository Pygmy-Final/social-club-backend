from django.shortcuts import render
from .models import Event
from .serializers import EventSerialzer
from rest_framework import generics
from .permissions import EventUserWritePermiss
from rest_framework.permissions import IsAuthenticated

class EventsList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerialzer
    permission_classes = [IsAuthenticated,]

class EventsDetail(generics.RetrieveUpdateDestroyAPIView,EventUserWritePermiss):
    queryset = Event.objects.all()
    serializer_class = EventSerialzer
    permission_classes = [EventUserWritePermiss,]