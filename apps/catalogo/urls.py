from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CatalogoViewSet,PlanosViewSet


router = DefaultRouter()
router.register(r'planos', PlanosViewSet,basename='planos')
router.register(r'', CatalogoViewSet,basename='catalogo')


urlpatterns = [
    path('', include(router.urls)),
]