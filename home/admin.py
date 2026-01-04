from django.contrib import admin
from .models import Funcionario

# Registrando o model Funcionario no painel administrativo
admin.site.register(Funcionario)