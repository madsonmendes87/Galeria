from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'galeria/home.html')

def cadastro(request):
    return render(request, 'galeria/cadastro.html')
