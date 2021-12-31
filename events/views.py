from django.shortcuts import render
from .models import Event
from .serializers import EventSerialzer
from rest_framework import generics
from .permissions import EventUserWritePermiss
from rest_framework.permissions import IsAuthenticated


class EventsList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerialzer
    # permission_classes = (IsAuthenticated,)

class EventsDetail(generics.RetrieveUpdateDestroyAPIView,EventUserWritePermiss):
    queryset = Event.objects.all()
    serializer_class = EventSerialzer
    # permission_classes = (EventUserWritePermiss,)





# class MessageDetailSerializer(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#     permission_classes = [IsAuthenticated,]

# class UserList(generics.ListCreateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#     permission_classes = [IsAuthenticated,]
# ==============================

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer

#     def get_permissions(self):
#         permission_classes = []
#         if self.action == 'create':
#             permission_classes = [AllowAny]
#         elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
#             permission_classes = [IsLoggedInUserOrAdmin]
#         elif self.action == 'list' or self.action == 'destroy':
#             permission_classes = [IsAdminUser]
#         return [permission() for permission in permission_classes]

# class CurrentUserView(APIView):
#     def get(self, request):
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data)

# class UserView(generics.RetrieveUpdateDestroyAPIView)