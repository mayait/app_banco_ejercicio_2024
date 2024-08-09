# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Cliente, Cuenta, Movimiento


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'cedula')


@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'saldo')
    list_filter = ('cliente',)


@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cuenta',
        'fecha_y_hora',
        'tipo',
        'monto',
        'descripcion',
    )
    list_filter = ('cuenta', 'fecha_y_hora')