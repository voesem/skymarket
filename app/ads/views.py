from rest_framework import pagination, viewsets, generics

from .models import Ad, Comment
from .serializers import AdSerializer, AdDetailSerializer


class AdPagination(pagination.PageNumberPagination):
    """ Настройки пагинации для объявлений """
    page_size = 4  # 4 объявления на странице


class AdListAPIView(generics.ListAPIView):
    """ Список объявлений. """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    pagination_class = AdPagination

    # def get_queryset(self):
    #     if self.request.user.role.filter(name='Модераторы').exists():
    #         return Ad.objects.all()  # Модераторам доступен список всех уроков
    #
    #     return Ad.objects.filter(author=self.request.user)  # Обычным пользователям доступны только их уроки


class AdCreateAPIView(generics.CreateAPIView):
    """ Создание объявления. """
    serializer_class = AdSerializer

    def perform_create(self, serializer):
        """ При создании объявления устанавливается связь с текущим пользователем. """
        serializer.save(author=self.request.user)


class AdRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр одного объявления. """
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()


class AdUpdateAPIView(generics.UpdateAPIView):
    """ Редактирование объявления. """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()


class AdDestroyAPIView(generics.DestroyAPIView):
    """ Удаление объявления. """
    queryset = Ad.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    pass
