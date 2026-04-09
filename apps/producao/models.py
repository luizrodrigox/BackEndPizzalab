from django.db import models
from apps.pedidos.models import Pedido

# Create your models here.

class Producao(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Producao {self.id}"