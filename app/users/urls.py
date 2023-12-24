from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import MyTokenObtainPairView

# Маршруты для представлений пользователей с использованием пакета Djoser
users_router = SimpleRouter()

users_router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(users_router.urls)),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
