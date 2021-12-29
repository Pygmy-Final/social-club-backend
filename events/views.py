from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Event

class EventsList(ListView):
    # queryset = User.objects.all()
    model=Event
    fields = ['EventName','EventCreator']

class EventsDetail(DetailView):
    # queryset = User.objects.all()
    model=Event
    fields = ['EventName','EventCategory','EventLocation','EventStartTime','EventDescription']
