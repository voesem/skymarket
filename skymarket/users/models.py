from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {'null': True, 'blank': True}


class UserRoles(models.TextChoices):
    """ Роли пользователей. """

    MEMBER = 'member', _('member')
    ADMIN = 'admin', _('admin')


class CustomUserManager(BaseUserManager):
    """ Кастомный менеджер для модели пользователя. """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """ Метод для создания пользователя с заданными email и паролем. """

        if not email:
            raise ValueError('Необходимо указать email.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """ Метод для создания обычного пользователя. """

        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """ Метод для создания суперпользователя. """

        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Cуперпользователь должен иметь флаг is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


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
