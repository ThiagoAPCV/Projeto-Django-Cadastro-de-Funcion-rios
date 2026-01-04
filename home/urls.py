from django.urls import path
from .views import index

# URLs específicas do app home
urlpatterns = [
    path('', index),
]
