from django.shortcuts import render
from .models import *
# Create your views here.
def index (request):
    
    mvv_var = mvv.objects.get()
    
    context = {
        'visao': mvv_var.visao,
        'valores': mvv_var.valores,
        'missao': mvv_var.missao,
    }
    
    return render(
        request, 
        'index.html', context
    )