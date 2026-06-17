from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet,ClienteViewSet

router = DefaultRouter()
router.register(r'', UsuarioViewSet, basename='usuarios')
router.register(r'clientes', ClienteViewSet,basename='clientes')

urlpatterns = [
    path('', include(router.urls)),
]