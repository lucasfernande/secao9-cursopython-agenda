from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.models import User


# Create your views here.

def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    nome = request.POST.get('nome')
    s_nome = request.POST.get('s_nome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    # verifica se tem campos vazios
    if not nome or not s_nome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Preencha todos os campos')
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido')
        return render(request, 'accounts/cadastro.html')

    if len(usuario) < 6:
        messages.error(request, 'Usuario precisa ter 6 caracteres ou mais')
        return render(request, 'accounts/cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais')
        return render(request, 'accounts/cadastro.html')

    if not senha == senha2:
        messages.error(request, 'Senhas não são iguais')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Este usuário já está cadastrado')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Este email já está cadastrado')
        return render(request, 'accounts/cadastro.html')

    messages.success(request, 'Cadastrado com sucesso!')

    user = User.objects.create_user(username=usuario,
                                    email=email,
                                    password=senha,
                                    first_name=nome,
                                    last_name=s_nome)

    user.save()
    return redirect('login')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
