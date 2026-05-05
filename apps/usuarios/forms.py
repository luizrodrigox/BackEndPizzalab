from django import forms
import bleach

class UsuarioForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length = 6)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return bleach.clean(email, tags = [], strip = True).strip()

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return bleach.clean(password, tags = [], strip = True).strip()