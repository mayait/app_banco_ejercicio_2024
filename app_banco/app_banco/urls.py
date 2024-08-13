
from django.contrib import admin
from django.urls import path, include
from cuentas.views import ver_movimientos, transferir, nuevo_cliente, ver_cliente, editar_cliente, home

urlpatterns = [
    path('accounts/', include('allauth.urls')),


    path('admin/', admin.site.urls),
    path('movimientos/<int:cuenta_id>', ver_movimientos, name='ver_movimientos_cuenta'),
    path('transferir', transferir, name='transferir'),
    path('cliente/nuevo', nuevo_cliente, name='nuevo_cliente'),
    path('cliente/<int:cliente_id>', ver_cliente, name='ver_cliente'),
    path('cliente/editar/<int:cliente_id>', editar_cliente, name='editar_cliente'),
    path('', home, name='home'),

]
