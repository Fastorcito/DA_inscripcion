# forms.py
from django import forms
from .models import Usuario, Aficion, Interes

class UsuarioForm(forms.ModelForm):
    aficiones = forms.ModelMultipleChoiceField(queryset=Aficion.objects.all(), widget=forms.CheckboxSelectMultiple)
    intereses = forms.ModelMultipleChoiceField(queryset=Interes.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Usuario
        fields = ['nombre', 'direccion', 'correo', 'contrasena', 'fecha_nacimiento', 'sexo']
