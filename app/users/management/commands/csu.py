from users.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    """ Кастомная команда для создания суперпользователя. """

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@skymarket.ru',
            first_name='Admin',
            last_name='Adminov',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('qauqazsyla01')
        user.save()
