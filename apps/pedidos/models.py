from django.db import models
from apps.clientes.models import Cliente
from apps.cardapio.models import Pizza

# Create your models here.

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pizzas = models.ManyToManyField(Pizza)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"Pedido {self.id}"