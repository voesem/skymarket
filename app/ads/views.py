from rest_framework import pagination, viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Ad, Comment
from .serializers import AdSerializer, AdDetailSerializer, CommentSerializer
from .permissions import IsOwner, IsAdmin


class AdPagination(pagination.PageNumberPagination):
    """ Настройки пагинации для объявлений """
    page_size = 4  # 4 объявления на странице


class AdListAPIView(generics.ListAPIView):
    """ Список объявлений. """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    pagination_class = AdPagination

    def get_queryset(self):
        if self.request.user.is_anonymous or self.request.user.role.filter(name='admin').exists():
            return Ad.objects.all()  # Администраторам и анонимным пользователям доступен список всех объявлений

        return Ad.objects.filter(author=self.request.user)  # Авторизованным пользователям доступны только их объявления


class MyAdListAPIView(generics.ListAPIView):
    """ Список объявлений пользователя. """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    permission_classes = [IsOwner]


class AdCreateAPIView(generics.CreateAPIView):
    """ Создание объявления. """
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """ При создании объявления устанавливается связь с текущим пользователем. """
        serializer.save(author=self.request.user)


class AdRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр одного объявления. """
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsOwner | IsAdmin]


class AdUpdateAPIView(generics.UpdateAPIView):
    """ Редактирование объявления. """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsOwner | IsAdmin]


class AdDestroyAPIView(generics.DestroyAPIView):
    """ Удаление объявления. """
    queryset = Ad.objects.all()
    permission_classes = [IsOwner | IsAdmin]


class CommentListAPIView(generics.ListAPIView):
    """ Список отзывов. """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(ad=self.kwargs.get('ad_pk'))


class CommentCreateAPIView(generics.CreateAPIView):
    """ Создание отзыва. """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """ При создании отзыва устанавливается связь с текущим пользователем и объявлением. """
        new_comment = serializer.save()
        new_comment.author = self.request.user
        new_comment.ad = Ad.objects.get(pk=self.kwargs.get('ad_pk'))
        new_comment.save()


class CommentRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр одного отзыва. """
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'com_pk'
    queryset = Comment.objects.all()
    permission_classes = [IsOwner | IsAdmin]


class CommentUpdateAPIView(generics.UpdateAPIView):
    """ Редактирование отзыва. """
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'com_pk'
    queryset = Comment.objects.all()
    permission_classes = [IsOwner | IsAdmin]


class CommentDestroyAPIView(generics.DestroyAPIView):
    """ Удаление отзыва. """
    queryset = Comment.objects.all()
    lookup_url_kwarg = 'com_pk'
    permission_classes = [IsOwner | IsAdmin]
