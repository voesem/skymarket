from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Ad(models.Model):
    """ Модель объявления. """

    title = models.CharField(max_length=200, verbose_name='название')
    price = models.IntegerField(verbose_name='цена')
    description = models.TextField(verbose_name='описание')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время и дата создания', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ('-created_at',)


class Comment(models.Model):
    """ Модель отзыва. """

    text = models.TextField(verbose_name='текст')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор', **NULLABLE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='объявление', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время и дата создания', **NULLABLE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-created_at',)
