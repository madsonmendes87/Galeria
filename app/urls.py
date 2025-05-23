from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro/usuarios/', views.usuarios, name='listagem_usuarios'),
    path('login/', views.login, name='login'),
]