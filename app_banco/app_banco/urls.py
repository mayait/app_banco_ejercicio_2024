"""
URL configuration for app_banco project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from cuentas.views import ver_movimientos, transferir, nuevo_cliente, ver_cliente, editar_cliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movimientos/<int:cuenta_id>', ver_movimientos, name='ver_movimientos_cuenta'),
    path('transferir', transferir, name='transferir'),
    path('cliente/nuevo', nuevo_cliente, name='nuevo_cliente'),
    path('cliente/<int:cliente_id>', ver_cliente, name='ver_cliente'),
    path('cliente/editar/<int:cliente_id>', editar_cliente, name='editar_cliente'),

]
