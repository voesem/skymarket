from django.contrib.auth.models import BaseUserManager


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
