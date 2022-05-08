from multiprocessing.sharedctypes import Value
from django.forms import ValidationError, modelformset_factory
from django.shortcuts import redirect,render
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import ContatoForm  
from django.core.paginator import Paginator 

def login(request):
    if request.method!='POST': 
        return render(request, 'accounts/login.html')
    
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    user = auth.authenticate(request, username=usuario,password=senha)
    print(user)

    if not user:
        messages.error(request, 'Usuário e/ou senha inválidos!')
        return redirect('login')
    
    else:
        auth.login(request, user)
        messages.success(request, 'Você fez login com sucesso.')
        return redirect('dashboard')
    

def register(request):
    if request.method!='POST': 
        return render(request, 'accounts/register.html')
    
    forms = {
        'nome':request.POST.get('nome'),
        'sobrenome':request.POST.get('sobrenome'),
        'idade': request.POST.get('idade'),
        'email': request.POST.get('email'),
        'usuario':request.POST.get('usuario'),
        'senha': request.POST.get('senha'),
        'senha2': request.POST.get('senha2')
    }

    for x in forms.values():
        if not x:
            messages.error(request,'Formulário incompleto! Por favor insira todas as informações corretamente!')
            return render(request, 'accounts/register.html')

    try:
        validate_email(forms['email'])
    except ValidationError:
        messages.error(request, 'Email Inválido!')
        return render(request, 'accounts/register.html')

    if forms['senha2'] != forms['senha']:
        messages.error(request, 'Senhas não batem, tente novamente!')
        return render(request, 'accounts/register.html')

    elif len(forms['senha'])<8:
        messages.error(request, 'Senha precisa ter mais de 8 caracteres')
        return render(request, 'accounts/register.html')
    
    elif User.objects.filter(username=forms['usuario']).exists():
        messages.error(request,'Usuário escolhido já existe.')
        return render(request, 'accounts/register.html')

    elif User.objects.filter(email=forms['email']).exists():
        messages.error(request,'Email escolhido já existe.')
        return render(request, 'accounts/register.html')
    
    elif int(forms['idade'])<12:
        messages.error(request, 'Desculpe, mas o Agenda Online só é permitido para maiores de 12 anos.')
        return render(request, 'accounts/register.html')

    else:
        user = User.objects.create_user(username=forms['usuario'],password=forms['senha'], email=forms['email'], first_name=forms['nome'], last_name=forms['sobrenome'] )
        user.save()

        
    messages.success(request, 'Usuário cadastrado com sucesso! Seja bem-vindo ao Agenda Online!')
    return redirect('login')


@login_required(redirect_field_name='index')
def dashboard(request):
    contatos = request.user.contato.all()
    contatos = Paginator(contatos, 8)
    num_pagina = request.GET.get('page')
    page_obj = contatos.get_page(num_pagina)
    return render(request, 'accounts/dashboard.html', {'page_obj':page_obj})
    

@login_required(redirect_field_name='index')
def dashboard_create(request):
    if request.method != 'POST':
        form = ContatoForm()
        return render(request,'accounts/dashboard_create.html', {'form': form})
    
    try:
        validate_email(request.POST.get('email'))
    except ValidationError:
        messages.warning(request, 'Endereço de email inválido!')
        form = ContatoForm(request.POST)
        return render(request,'accounts/dashboard_create.html', {'form': form})

    try:
        int(request.POST.get('telefone'))
    except ValueError:
        messages.warning(request,'Digite apenas números no campo telefone')
        form = ContatoForm(request.POST)
        return render(request,'accounts/dashboard_create.html', {'form': form})

    form = ContatoForm(request.POST,request.FILES)
    form_validator = form.save(commit=False)
    form_validator.user = request.user
    form_validator.save()

    if form.is_valid():
        form.save()
    
    else:
        messages.error(request, 'Não foi possível enviar o formulário.')
        form = ContatoForm(request.POST)
        return render(request,'accounts/dashboard_create.html', {'form': form})

    messages.success(request, 'Contato criado.')
    return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('login')


def ver_contato(request, contato_id):
    contato = request.user.contato.get(id=contato_id)
    return render(request,'accounts/ver_contato.html', {'contato': contato})

# Create your views here.
 