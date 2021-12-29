from .views import  EventsDetail , EventsList
from django.urls import path

urlpatterns=[
    path('', EventsList.as_view(),name='event_list')
]