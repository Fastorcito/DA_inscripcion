from django.shortcuts import render, redirect
from .models import UsuarioAficion, UsuarioInteres
from .forms import UsuarioForm

# Create your views here.
def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()

            for aficion in form.cleaned_data['aficiones']:
                UsuarioAficion.objects.create(id_usuario=usuario, id_aficion=aficion)

            for interes in form.cleaned_data['intereses']:
                UsuarioInteres.objects.create(id_usuario=usuario, id_interes=interes)

            return redirect('confirmacion_inscripcion') 
    else:
        form = UsuarioForm()

    return render(request, 'registrar_usuario.html', {'form': form})