from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Cuenta, Movimiento, Cliente
import decimal


def ver_movimientos(request, cuenta_id):
    cuenta = get_object_or_404(Cuenta, id = cuenta_id)
    movimientos = cuenta.movimientos.all()
    contenido = {
        'cuenta': cuenta,
        'movimientos': movimientos
    }

    return render(request, 'movimientos.html', contenido)

def transferir(request):
    if request.method == "POST":
        print("✅ POST:", request.POST)
        monto= decimal.Decimal(float(request.POST['monto']))
        cuenta_destino_id = int(request.POST['cuenta_destino'])
        cuenta_destino = get_object_or_404(Cuenta, id=cuenta_destino_id)
        cuenta_origen_id = int(request.POST['cuenta_origen'])
        cuenta_origen = get_object_or_404(Cuenta, id=cuenta_origen_id)
        cuenta_origen.transferir(monto, cuenta_destino, request.POST['descripcion'])

        return HttpResponse("Transferencia realizada")
    return HttpResponse("Metodo incorrecto")
