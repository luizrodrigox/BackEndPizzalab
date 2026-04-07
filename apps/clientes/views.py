from django.http import JsonResponse
from .models import Cliente
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def criar(request):
    if request.method == "POST":
        data = json.loads(request.body)
        cliente = Cliente.objects.create(
            nome = data["nome"],
            telefone = data["telefone"]
        )
        return JsonResponse({"id": cliente.id})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)


def listar(request):
    if request.method == "GET":
        return JsonResponse(list(Cliente.objects.values()), safe = False)
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)


def detalhe(request, id):
    if request.method == "GET":
        cliente = Cliente.objects.filter(id = id).values().first()
        return JsonResponse(cliente or {"erro": "Não encontrado"})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)

@csrf_exempt
def atualizar(request, id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            cliente = Cliente.objects.get(id = id)
            cliente.nome = data["nome"]
            cliente.telefone = data["telefone"]
            cliente.save()
            return JsonResponse({"msg": "Atualizado"})
        except Cliente.DoesNotExist:
            return JsonResponse({"erro": "Não encontrado"})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)

@csrf_exempt
def deletar(request, id):
    if request.method == "DELETE":
        try:
            Cliente.objects.get(id = id).delete()
            return JsonResponse({"msg": "Deletado"})
        except Cliente.DoesNotExist:
            return JsonResponse({"erro": "Não encontrado"})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)