from django.http import JsonResponse
from .models import Pizza
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def criar(request):
    if request.method == "POST":
        data = json.loads(request.body)
        pizza = Pizza.objects.create(
            nome = data["nome"],
            preco = data["preco"]
        )
        return JsonResponse({"id": pizza.id})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)


def listar(request):
    if request.method == "GET":
        return JsonResponse(list(Pizza.objects.values()), safe = False)
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)


def detalhe(request, id):
    if request.method == "GET":
        pizza = Pizza.objects.filter(id = id).values().first()
        return JsonResponse(pizza or {"erro": "Não encontrada"})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)

@csrf_exempt
def atualizar(request, id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            pizza = Pizza.objects.get(id = id)
            pizza.nome = data["nome"]
            pizza.preco = data["preco"]
            pizza.save()
            return JsonResponse({"msg": "Atualizado"})
        except Pizza.DoesNotExist:
            return JsonResponse({"erro": "Não encontrada"})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)

@csrf_exempt
def deletar(request, id):
    if request.method == "DELETE":
        try:
            Pizza.objects.get(id = id).delete()
            return JsonResponse({"msg": "Deletado"})
        except Pizza.DoesNotExist:
            return JsonResponse({"erro": "Não encontrada"})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)