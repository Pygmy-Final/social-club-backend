from django.urls import path
from .views import MessageView, MessageDetailView
# from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    # path('', views.homepage, name="home"),
    # path('login/', LoginView.as_view(), name="login"),
    # path('logout/', LogoutView.as_view(), name="logout"),
    # path('register/', views.register, name="register"),
    path("", MessageView.as_view(), name="message_list"),
    path("<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
]


# ************ test message view with int:pk