from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'perfiles',PerfilesVS,basename='perfil')
router.register(r'modulos',ModuloVS,basename='modulo')
router.register(r'permisos',PermisoVS,basename='permiso')
router.register(r'login',LoginNoir,basename='login')

urlpatterns = [
    path('', include(router.urls)),
    path('crear-usuario/', crear_nuevo_usuario),
]