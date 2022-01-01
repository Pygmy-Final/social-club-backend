from .views import UserProfileDetailView, UserProfileListView, UserProfileCreateView, FollowListView, FollowCreateView
from django.urls import path

urlpatterns=[
    path('', UserProfileListView.as_view(), name='user_list'),
    path('<int:pk>/', UserProfileDetailView.as_view(), name='user_detail'),
    path('create-user/',UserProfileCreateView.as_view(), name='create_user'),
    path('user-follow/', FollowListView.as_view(), name='user_follow'),
    path('add-follow/', FollowCreateView.as_view(), name='add_follow'),
]