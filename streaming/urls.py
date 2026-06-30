"""
URL configuration for streaming project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import UsuarioViewSet, ClienteViewSet, ClienteCreateView, AssinaturaDetailView, UsuarioUpdateView

router = DefaultRouter()
router.register(r'', UsuarioViewSet, basename='usuarios')
router.register(r'clientes', ClienteViewSet, basename='clientes')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/catalogo/', include('apps.catalogo.urls')),
    path('api/filmes/', include('apps.filmes.urls')),
    path('api/usuarios/', include('apps.usuarios.urls')),
    path('clientes/add/', ClienteCreateView.as_view(), name='adicionar-cliente'),
    path('clientes/<int:pk>/assinatura/', AssinaturaDetailView.as_view(), name='visualizar-assinatura'),
    path('<int:pk>/update/', UsuarioUpdateView.as_view(), name='atualizar-perfil'),
]

