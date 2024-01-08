from django.urls import path

from .apps import SalesConfig
from .views import (AdListAPIView, AdCreateAPIView, AdRetrieveAPIView, AdUpdateAPIView, AdDestroyAPIView,
                    MyAdListAPIView, CommentListAPIView, CommentCreateAPIView, CommentRetrieveAPIView,
                    CommentUpdateAPIView, CommentDestroyAPIView)

# Маршруты для представлений моделей Ad и Comment

app_name = SalesConfig.name

urlpatterns = [
    path('', AdListAPIView.as_view(), name='ads_list'),
    path('create/', AdCreateAPIView.as_view(), name='create_ad'),
    path('me/', MyAdListAPIView.as_view(), name='my_ads_list'),
    path('<int:ad_pk>/', AdRetrieveAPIView.as_view(), name='get_ad'),
    path('<int:ad_pk>/update/', AdUpdateAPIView.as_view(), name='update_ad'),
    path('<int:ad_pk>/delete/', AdDestroyAPIView.as_view(), name='delete_ad'),

    path('<int:ad_pk>/comments/', CommentListAPIView.as_view(), name='comments_list'),
    path('<int:ad_pk>/comments/create/', CommentCreateAPIView.as_view(), name='create_comment'),
    path('<int:ad_pk>/comments/<int:com_pk>/', CommentRetrieveAPIView.as_view(), name='get_comment'),
    path('<int:ad_pk>/comments/<int:com_pk>/update/', CommentUpdateAPIView.as_view(), name='update_comment'),
    path('<int:ad_pk>/comments/<int:com_pk>/delete/', CommentDestroyAPIView.as_view(), name='update_comment'),
]
