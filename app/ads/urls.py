from django.urls import include, path

from .apps import SalesConfig
from .views import AdListAPIView, AdCreateAPIView, AdRetrieveAPIView, AdUpdateAPIView, AdDestroyAPIView

# Маршруты для представлений моделей Ad и Comment

app_name = SalesConfig.name

urlpatterns = [
    path('', AdListAPIView.as_view(), name='ads_list'),
    path('create/', AdCreateAPIView.as_view(), name='create_ad'),
    path('<int:pk>/', AdRetrieveAPIView.as_view(), name='get_ad'),
    path('<int:pk>/update/', AdUpdateAPIView.as_view(), name='update_ad'),
    path('<int:pk>/delete/', AdDestroyAPIView.as_view(), name='delete_ad'),
]
