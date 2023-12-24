from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    """ Получение токена при авторизации """

    serializer_class = MyTokenObtainPairSerializer
