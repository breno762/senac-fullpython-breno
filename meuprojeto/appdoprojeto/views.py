from django.shortcuts import render
from .models import Produto

def home(request):
    return render(request, 'appdoprojeto/home.html')

def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'appdoprojeto/produtos.html', {'produtos': produtos})



