from django.contrib import admin
from django.urls import path, include

# Mapa principal de URLs do projeto
urlpatterns = [
    # Painel administrativo
    path('admin/', admin.site.urls),

    # URLs do app home
    path('', include('home.urls')),
]
