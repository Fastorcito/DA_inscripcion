from django.contrib import admin
from .models import Aficion, Interes, Usuario, UsuarioAficion, UsuarioInteres
# Register your models here.
admin.site.register(Aficion)
admin.site.register(Interes)
admin.site.register(Usuario)
admin.site.register(UsuarioAficion)
admin.site.register(UsuarioInteres)

