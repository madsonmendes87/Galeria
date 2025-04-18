from django.shortcuts import render
from .models import Usuario
# Create your views here.
def home(request):
    return render(request, 'galeria/home.html')

def cadastro(request):
    return render(request, 'galeria/cadastro.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.usuario = request.POST.get('usuario')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.casal = request.POST.get('casal')
    novo_usuario.save()

    usuarios = {
    'usuarios': Usuario.objects.all()
    }
    return render(request, 'galeria/usuarios.html', usuarios)
