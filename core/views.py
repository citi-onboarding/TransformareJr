from django.shortcuts import render
from .models import *
# Create your views here.
def index (request):
    
    editaveis_var = editavei.objects.get()
    
    context = {
        'visao': editaveis_var.visao,
        'valores': editaveis_var.valores,
        'missao': editaveis_var.missao,
        'telefone': editaveis_var.telefone,
    }
    
    return render(
        request, 
        'index.html', context
    )