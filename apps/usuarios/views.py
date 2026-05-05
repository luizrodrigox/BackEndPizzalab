from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .forms import UsuarioForm

@csrf_exempt
def register(request):
    if request.method == "POST":

        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"erro": "JSON inválido"}, status = 400)

        form = UsuarioForm(data)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            if User.objects.filter(username = email).exists():
                return JsonResponse({"erro": "Usuário já existe"}, status = 400)

            User.objects.create_user(
                username = email,
                password = password
            )

            return JsonResponse({"msg": "Usuário criado"})

        return JsonResponse(form.errors, status = 400)

    return JsonResponse({"erro": "Método não permitido"}, status = 405)


@csrf_exempt
def login(request):
    if request.method == "POST":

        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"erro": "JSON inválido"}, status = 400)

        form = UsuarioForm(data)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = authenticate(username = email, password = password)

            if user:
                refresh = RefreshToken.for_user(user)

                return JsonResponse({
                    "access": str(refresh.access_token)
                })

            return JsonResponse({"erro": "Credenciais inválidas"}, status = 401)

        return JsonResponse(form.errors, status = 400)

    return JsonResponse({"erro": "Método não permitido"}, status = 405)