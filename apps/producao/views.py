from django.http import JsonResponse
from .models import Producao
from apps.pedidos.models import Pedido
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def criar(request):
    if request.method == "POST":
        data = json.loads(request.body)

        pedido = Pedido.objects.get(id = data["pedido_id"])
        prod = Producao.objects.create(
            pedido = pedido,
            status = data["status"]
        )

        return JsonResponse({"id": prod.id})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)


def listar(request):
    if request.method == "GET":
        return JsonResponse(list(Producao.objects.values()), safe = False)
    
    return JsonResponse({"erro": "Método não permitido"}, statu = 405)


def detalhe(request, id):
    if request.method == "GET":
        try:
            prod = Producao.objects.get(id = id)
            return JsonResponse({
                "id": prod.id,
                "pedido_id": prod.pedido.id,
                "status": prod.status
            })
        except Producao.DoesNotExist:
            return JsonResponse({"erro": "Não encontrado"})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)

@csrf_exempt
def atualizar(request, id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            prod = Producao.objects.get(id = id)
            prod.status = data["status"]
            prod.save()
            return JsonResponse({"msg": "Atualizado"})
        except Producao.DoesNotExist:
            return JsonResponse({"erro": "Não encontrado"})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)

@csrf_exempt
def deletar(request, id):
    if request.method == "DELETE":
        try:
            Producao.objects.get(id = id).delete()
            return JsonResponse({"msg": "Deletado"})
        except Producao.DoesNotExist:
            return JsonResponse({"erro": "Não encontrado"})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)