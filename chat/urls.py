from django.urls import path
from .views import MessageView, MessageDetailView

urlpatterns = [
    path("", MessageView.as_view(), name="message_list"),
    path("<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
]

