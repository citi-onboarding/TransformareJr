from django.shortcuts import render
from templated_email import send_templated_mail
from .models import *
# Create your views here.
def index (request):

    editaveis_var = editavei.objects.first()
    
    context = {
        'visao': editaveis_var.visao,
        'valores': editaveis_var.valores,
        'missao': editaveis_var.missao,
        'email': editaveis_var.email,
        'telefone': editaveis_var.telefone,
    } 
    
    if request.method == 'POST':
        nome=request.POST.get('nome')
        email=request.POST.get('email')
        telefone=request.POST.get('telefone')
        conheceu=request.POST.get('conheceu')
        assunto=request.POST.get('assunto')
        mensagem=request.POST.get('mensagem')
        send_templated_mail(
        template_name='email',
        from_email= email,
        recipient_list=['contato.transformarejr@gmail.com'],
        context={
            'nome':nome,
            'email':email,
            'telefone':telefone,
            'conheceu':conheceu,
            'assunto':assunto,
            'mensagem':mensagem
        },)



    return render(
        request, 
        'index.html', context
    )