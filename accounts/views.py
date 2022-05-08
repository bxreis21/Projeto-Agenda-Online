from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.validators import validate_email

def login(request):
    if request.method!='POST': 
        return render(request, 'accounts/login.html')
    

def register(request):
    if request.method!='POST': 
        return render(request, 'accounts/register.html')
    
    forms = {
        'nome':request.POST.get('nome'),
        'sobrenome':request.POST.get('sobrenome'),
        'telefone': request.POST.get('telefone'),
        'idade': request.POST.get('idade'),
        'email': request.POST.get('email'),
        'senha': request.POST.get('senha'),
        'senha2': request.POST.get('senha2')
    }

    for x in forms.values():
        if not x:
            messages.error(request,'Formulário incompleto! Por favor insira as informações corretamente!')
            return render(request, 'accounts/register.html')

    try:
        validate_email(forms['email'])
    except ValidationError:
        messages.error(request, 'Email Inválido!')
        return render(request, 'accounts/register.html')

    if forms['senha2'] != forms['senha']:
        messages.error(request, 'Senhas não batem, tente novamente!')
        return render(request, 'accounts/register.html')
        
    messages.success(request, 'Usuário cadastrado com sucesso! Seja bem-vindo ao Agenda Online!')

    return redirect('login')

# Create your views here.
 