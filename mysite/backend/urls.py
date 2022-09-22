from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'perfiles',PerfilesVS,basename='perfil')
router.register(r'usuarios',UserVS,basename='user')
router.register(r'modulos',ModuloVS,basename='modulo')
router.register(r'comisiones',ComisionVS,basename='comision')
router.register(r'permisos',PermisoVS,basename='permiso')
router.register(r'login',LoginNoir,basename='login')

urlpatterns = [
    path('', include(router.urls)),
    path('crear-usuario/', crear_nuevo_usuario),
    path('get-users-defix', get_users_defix),
    path('get-users-admin', get_users_admin),
    path('get-transaction-history', get_transaction_history),
    path('get-balance-defix', get_balance_defix),
    path('act-user-admin', actualizar_usuario_admin),
    path('get-comision/<str:coin>', get_comision)
]