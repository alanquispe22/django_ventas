from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=15)
    paterno = models.CharField(max_length=15)
    materno = models.CharField(max_length=15)
    
class Venta(models.Model):
    fecha_venta = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Producto(models.Model):
    descripcion = models.CharField(max_length=30)
    precio = models.PositiveIntegerField()
    ventas = models.ManyToManyField(Venta, through='Producto_venta')
    
class Producto_venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    descuento = models.PositiveIntegerField()