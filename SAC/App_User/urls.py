from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.formulario_novo_user, name='cad_usuario'),
    path('salvar_usuario', views.cadastrar_usuario, name='salvar_usuario'),
]
