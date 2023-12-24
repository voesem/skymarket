from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()
# Сериализаторы регистрации и просмотра профиля пользователя


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
            'phone',
        )


class CurrentUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone',
            'image',
        )


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email

        return token
