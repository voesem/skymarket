# Generated by Django 3.2.6 on 2023-12-22 09:26

from django.db import migrations, models
import phonenumber_field.modelfields
import users.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='почта')),
                ('first_name', models.CharField(max_length=200, verbose_name='имя')),
                ('last_name', models.CharField(max_length=200, verbose_name='фамилия')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=12, region='RU', verbose_name='номер телефона')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='аватар')),
                ('role', models.CharField(choices=[('member', 'member'), ('admin', 'admin')], default='member', max_length=6, verbose_name='роль пользователя')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', users.managers.CustomUserManager()),
            ],
        ),
    ]
