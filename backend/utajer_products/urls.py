from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter(trailing_slash=False)

router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
]