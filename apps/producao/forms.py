from django import forms
from .models import Producao
import bleach

class ProducaoForm(forms.ModelForm):
    class Meta:
        model = Producao
        fields = ['pedido', 'status']

    def clean_status(self):
        status = self.cleaned_data.get('status')

        if not status:
            raise forms.ValidationError("Status obrigatório")

        return bleach.clean(status, tags=[], strip=True).strip()