# Generated by Django 3.2.6 on 2024-01-08 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_auto_20231222_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='ad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.ad', verbose_name='объявление'),
        ),
    ]
