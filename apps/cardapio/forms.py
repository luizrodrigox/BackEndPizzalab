from django import forms
from .models import Pizza
import bleach

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['nome', 'preco']

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')

        if not nome:
            raise forms.ValidationError("Nome obrigatório")

        return bleach.clean(nome, tags=[], strip=True).strip()

    def clean_preco(self):
        preco = self.cleaned_data.get('preco')

        if preco is None:
            raise forms.ValidationError("Preço obrigatório")

        if preco <= 0:
            raise forms.ValidationError("Preço inválido")

        return preco