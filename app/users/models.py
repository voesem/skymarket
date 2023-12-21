from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from users.managers import CustomUserManager

NULLABLE = {'null': True, 'blank': True}


class UserRoles(models.TextChoices):
    """ Роли пользователей. """

    MEMBER = 'member', _('member')
    ADMIN = 'admin', _('admin')


class User(AbstractUser):
    """ Модель пользователя """

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    first_name = models.CharField(max_length=200, verbose_name='имя')
    last_name = models.CharField(max_length=200, verbose_name='фамилия')
    phone = PhoneNumberField(max_length=12, region='RU', verbose_name='номер телефона')
    image = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    role = models.CharField(
        max_length=6,
        choices=UserRoles.choices,
        default=UserRoles.MEMBER,
        verbose_name='роль пользователя'
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
