# forms.py
from django import forms
from .models import Usuario, Aficion, Interes

class UsuarioForm(forms.ModelForm):
    confirmar_contrasena = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': True}))
    class Meta:
        model = Usuario
        fields = ['nombre', 'direccion', 'correo', 'contrasena', 'fecha_nacimiento', 'sexo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
            'contrasena': forms.PasswordInput(attrs={'class': 'form-control', 'required': True}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': True}),
            'sexo': forms.Select(attrs={'class': 'form-control'}, choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')]),
        }

    aficiones = forms.ModelMultipleChoiceField(queryset=Aficion.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
    intereses = forms.ModelMultipleChoiceField(queryset=Interes.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))

    def clean(self):
        cleaned_data = super().clean()
        contrasena = cleaned_data.get("contrasena")
        confirmar_contrasena = cleaned_data.get("confirmar_contrasena")

        if contrasena != confirmar_contrasena:
            self.add_error('confirmar_contrasena', "Las contraseñas no coinciden.")