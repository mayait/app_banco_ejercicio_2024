from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class Cuenta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cuentas')
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    def transferir(self, monto, cuenta_destino, descripcion):
        if self.saldo < monto:
            print("Saldo insuficiente")
            return
        self.retirar(monto, f"Transferencia a cuenta {cuenta_destino.id} por {descripcion}")
        cuenta_destino.depositar(monto, f"Transferencia de cuenta {self.id} por {descripcion}")


    def depositar(self, monto, descripcion):
        self.saldo = self.saldo + monto
        self.save()
        movimiento = Movimiento.objects.create(
            cuenta=self,
            tipo='deposito',
            monto=monto,
            descripcion=descripcion
        )
        movimiento.save()
    
    def retirar(self, monto, descripcion):
        if self.saldo >= monto:
            self.saldo = self.saldo - monto
            movimiento = Movimiento.objects.create(
                cuenta=self,
                tipo='retiro',
                monto=monto,
                descripcion=descripcion
            )
            movimiento.save()
        else:
            print("Saldo insuficiente")

    def __str__(self):
        return f"{self.id} {self.cliente}"
    
    

class Movimiento(models.Model):
    TIPO_MOVIMIENTOS = [
        ('deposito', 'Deposito'),
        ('retiro', 'Retiro')
    ]
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='movimientos')
    fecha_y_hora = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=20, choices=TIPO_MOVIMIENTOS)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
        

    def __str__(self):
        return f"Cuenta {self.cuenta.id} {self.tipo} ${self.monto}"
