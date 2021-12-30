from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
    path('events/',include('events.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name = 'token_refresh'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
