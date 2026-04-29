from django import forms
from .models import Pedido
import bleach

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'status']

    def clean_status(self):
        status = self.cleaned_data.get('status')

        if not status:
            raise forms.ValidationError("Status obrigatório")

        return bleach.clean(status, tags=[], strip=True).strip()