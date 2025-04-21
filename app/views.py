from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
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

def login(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            return render(request,'galeria/login.html')
        else:
            messages.info(request,'invalido credenciais')
            return redirect('/app')
    else:
        return render(request, 'galeria/home.html')
