from .views import UserProfileDetailView, UserProfileListView
from django.urls import path

urlpatterns=[
    path('', UserProfileListView.as_view(), name='user_list'),
    path('<int:pk>/', UserProfileDetailView.as_view(), name='user_detail'),
]