from .serializers import MessageSerializer
from .models import  Message
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter

class MessageView(generics.ListCreateAPIView):
    # queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends= [SearchFilter]
    search_fields = ['from_user']

    def  get_queryset(self, *args, **kwargs):
        user_id = str(self.request.user) 
        queryset = Message.objects.filter(sender = user_id)
        return queryset

class MessageDetailView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated,]

