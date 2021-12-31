from .views import UserProfileDetailView, UserProfileListView, UserProfileCreateView, FollowListView
from django.urls import path

urlpatterns=[
    path('', UserProfileListView.as_view(), name='user_list'),
    path('create-user/',UserProfileCreateView.as_view(), name='create_user'),
    path('<int:pk>/', UserProfileDetailView.as_view(), name='user_detail'),
    path('user-follow/', FollowListView.as_view(), name='user_follow'),
]