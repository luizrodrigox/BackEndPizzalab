from django import forms
from .models import Cliente
import bleach

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone']

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')

        if not nome:
            raise forms.ValidationError("Nome obrigatório")

        return bleach.clean(nome, tags=[], strip=True).strip()

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')

        if not telefone:
            raise forms.ValidationError("Telefone obrigatório")

        return telefone