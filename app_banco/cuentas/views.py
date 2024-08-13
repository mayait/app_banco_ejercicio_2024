from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Cuenta, Movimiento, Cliente
from .forms import ClienteForm
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



def ver_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    contenido = {
        'cliente': cliente,
    }
    return render(request, 'cliente.html', contenido)


def nuevo_cliente(request):
    mensaje_error = ""
    # Procesa el formulario para un nuevo cliente
    if request.method == "POST":
        # Crear el formulario con los datos del POST
        formulario = ClienteForm(request.POST)
        # Validar el formulario
        if formulario.is_valid():
            # Crear un nuevo cliente con los datos del formulario
            cliente = Cliente.objects.create(
                nombre=formulario.cleaned_data['nombre'],
                apellido=formulario.cleaned_data['apellido'],
                cedula=formulario.cleaned_data['cedula']
            )
            cliente.save()
            # TODO: redirigir a una pagina del cliente nuevo.
            return HttpResponseRedirect(reverse("ver_cliente", args=[cliente.id]))
        else:
            # TODO: Mostrar un mensaje de error, mantenerse en el formulario.
            mensaje_error = "Error en el formulario"
    else:
        # Crear un formulario vacio
        formulario = ClienteForm()
    # Renderizar el formulario
    return render(request, 'nuevo_cliente.html', {'formulario': formulario, 'mensaje_error': mensaje_error})


def editar_cliente(request, cliente_id):
    ## NO FUNCIONA
    ## NO PUEDO PASAR LA INSTANCIA DEL CLIENTE AL FORMULARIO
    
    mensaje_error = ""
    cliente = get_object_or_404(Cliente, id=cliente_id)
    # Procesa el formulario para un nuevo cliente
    if request.method == "POST":
        # Crear el formulario con los datos del POST
        formulario = ClienteForm(request.POST, instance=cliente)
        # Validar el formulario
        if formulario.is_valid():
            cliente.nombre = formulario.cleaned_data['nombre']
            cliente.apellido = formulario.cleaned_data['apellido']
            cliente.cedula = formulario.cleaned_data['cedula']
            cliente.save()
            # TODO: redirigir a una pagina del cliente nuevo.
            return HttpResponseRedirect(reverse("ver_cliente", args=[cliente.id]))
        else:
            # TODO: Mostrar un mensaje de error, mantenerse en el formulario.
            mensaje_error = "Error en el formulario"
    else:
        # Crear un formulario vacio
        formulario = ClienteForm(instance=cliente)
    # Renderizar el formulario
    return render(request, 'nuevo_cliente.html', {'formulario': formulario, 'mensaje_error': mensaje_error})