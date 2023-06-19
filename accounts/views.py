from django.contrib import messages, auth
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from string import ascii_letters
from .models import FormAdministrador, FormAlunoPcd, FormMonitor, FormTutor
from membros.forms import AlunosForm
# Create your views here.


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'usuario ou senha invalidos.')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.error(request, 'Login com sucesso.')
        return redirect('aviIndexAluno')

def logout(request):
    auth.logout(request)
    return redirect('dashboard')

def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    usuario = request.POST.get('cpf')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not usuario or not email or not senha or not senha2:
        messages.error(request, 'Todos os campos devem ser preenchidos')
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email invalido.')
        return render(request, 'accounts/cadastro.html')



    if len(usuario) > 14:
        messages.error(request, 'Cpf deve ter 14 caracteres.')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Cpf ja cadastrado, verifique e tente novamente!')
        return render(request, 'accounts/cadastro.html')


    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email ja cadastrado')
        return render(request, 'accounts/cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/cadastro.html')

    if senha != senha2:
        messages.error(request, 'Confirme as SENHAS novamente!')
        return render(request, 'accounts/cadastro.html')

    messages.success(request, 'Registrado com sucesso! Agora faca login.')

    user = User.objects.create_user(username=usuario, email=email,
                                    password=senha, first_name=nome,
                                    last_name=sobrenome)
    user.save()
    return redirect('login')



@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormAdministrador()
        return render(request, 'accounts/dashboard.html', {'form': form})

    form = FormAdministrador(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar suas informacoes')
        form = FormAdministrador(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    nome = request.POST.get('adm_nome')
    if len(nome) < 5:
        messages.error(request, '"Nome" deve ter que 5 caracteres')
        form = FormAdministrador(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    form.save()
    messages.success(request, f'Usuario {request.POST.get("adm_nome")} salvo com sucesso!')
    return redirect('dashboard')

@login_required(redirect_field_name='login')
def cadastroInterprete(request):
    if request.method != 'POST':
        form = FormAdministrador()
        return render(request, 'accounts/cadastroInterprete.html', {'form': form})

    form = FormAdministrador(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar suas informacoes, tente novamente!')
        form = FormAdministrador(request.POST)
        return render(request, 'accounts/cadastroInterprete.html', {'form': form})

    nome = request.POST.get('adm_nome')
    if len(nome) < 5:
        messages.error(request, '"Nome" deve ter que 5 caracteres')
        form = FormAdministrador(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    form.save()
    messages.success(request, f'Usuario {request.POST.get("adm_nome")} salvo com sucesso!')
    return redirect('dashboard')

def cadastroAluno(request):
    if request.method != 'POST':
        form = AlunosForm()
        return render(request, 'accounts/cadastroAluno.html', {'form': form})

    form = AlunosForm(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Informações invalidas, tente novamente!')
        form = AlunosForm(request.POST)
        return render(request, 'accounts/cadastroAluno.html', {'form': form})


    nome = request.POST.get('alu_nome')
    usuario = request.POST.get('alu_cpf')
    data_nascimento = request.POST.get('alu_data_nascimento')
    sexo = request.POST.get('alu_genero')
    email_pessoal = request.POST.get('alu_email_pessoal')
    email_instituicao = request.POST.get('alu_email_institucional')
    telefone = request.POST.get('alu_telefone')
    cep = request.POST.get('alu_endereco_cep')
    descricao_des = request.POST.get('alu_endereco_descricao')
    cidade = request.POST.get('alu_endereco_cidade')
    curso = request.POST.get(' alu_curso')
    periodo = request.POST.get('alu_periodo_academico')
    matricula = request.POST.get('alu_matricula')
    deficiencias = request.POST.get('alu_deficiencias')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not usuario or not data_nascimento or not sexo or not email_pessoal or not email_instituicao or not telefone or not cep or not descricao_des or not cidade or not periodo or not matricula or not senha or not senha2:
        messages.error(request, 'Todos os campos devem ser preenchidos!')
        return render(request, 'accounts/cadastroAluno.html',  {'form': form})

    try:
        valida_string(nome)
    except:
        messages.error(request, 'Por favor digite somente letras e espaços')
        return render(request, 'accounts/cadastroAluno.html',  {'form': form})

    try:
        validate_email(email_pessoal)
    except:
        messages.error(request, 'Email pessoal invalido!')
        return render(request, 'accounts/cadastroAluno.html',  {'form': form})

    try:
        validate_email(email_instituicao)
    except:
        messages.error(request, 'Email institucional invalido!')
        return render(request, 'accounts/cadastroAluno.html',  {'form': form})

    try:
         valida_cpf(usuario)
    except:
        messages.error(request, 'O Cpf informado não é valido, tente novamente!')
        return render(request, 'accounts/cadastroAluno.html', {'form': form})

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Cpf já cadastrado, verifique e tente novamente!')
        return render(request, 'accounts/cadastroAluno.html',  {'form': form})


    if User.objects.filter(email=email_pessoal).exists():
        messages.error(request, 'Email pessoal já cadastrado, tente novamente!')
        return render(request, 'accounts/cadastroAluno.html',  {'form': form})

    if User.objects.filter(email=email_instituicao).exists():
        messages.error(request, 'Email institucional já cadastrado, tente novamente!')
        return render(request, 'accounts/cadastroAluno.html',  {'form': form})

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter 7 caracteres ou mais.')
        return render(request, 'accounts/cadastroAluno.html',  {'form': form})

    if senha != senha2:
        messages.error(request, 'Senhas diferentes, tente novamente!')
        return render(request, 'accounts/cadastroAluno.html')

    messages.success(request, 'Cadastro com sucesso, realize seu primeiro Login!')

    user = User.objects.create_user(username=usuario, email=email_pessoal,
                                    password=senha, first_name=nome,
                                    last_name=email_instituicao)
    form.save()
    user.save()
    return redirect('login')

def cadastroMonitor(request):
    if request.method != 'POST':
        form = FormMonitor()
        return render(request, 'accounts/cadastroMonitor.html', {'form': form})

    form = FormMonitor(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar suas informacoes, tente novamente!')
        form = FormMonitor(request.POST)
        return render(request, 'accounts/cadastroMonitor.html', {'form': form})


    nome = request.POST.get('mon_nome')
    usuario = request.POST.get('mon_cpf')
    sexo = request.POST.get('mon_genero')
    email_pessoal = request.POST.get('mon_email_pessoal')
    email_instituicao = request.POST.get('mon_email_institucional')
    telefone = request.POST.get('mon_telefone')
    cep = request.POST.get('mon_endereco_cep')
    descricao_des = request.POST.get('mon_endereco_descricao')
    cidade = request.POST.get('mon_endereco_cidade')
    curso = request.POST.get(' mon_curso')
    periodo = request.POST.get('mon_periodo_academico')
    matricula = request.POST.get('mon_matricula')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not usuario or not sexo or not email_pessoal or not email_instituicao or not telefone or not cep or not descricao_des or not cidade or not periodo or not matricula or not senha or not senha2:
        messages.error(request, 'Todos os campos devem ser preenchidos!')
        return render(request, 'accounts/cadastroMonitor.html', {'form': form})

    try:
        validate_email(email_pessoal)
    except:
        messages.error(request, 'Email pessoal invalido!')
        return render(request, 'accounts/cadastroMonitor.html', {'form': form})

    try:
        validate_email(email_instituicao)
    except:
        messages.error(request, 'Email institucional invalido!')
        return render(request, 'accounts/cadastroMonitor.html', {'form': form})

    if len(usuario) > 14:
        messages.error(request, '')
        return render(request, 'accounts/cadastroMonitor.html', {'form': form})

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Cpf ja cadastrado, verifique e tente novamente!')
        return render(request, 'accounts/cadastroMonitor.html', {'form': form})

    if User.objects.filter(email=email_pessoal).exists():
        messages.error(request, 'Email pessoal ja cadastrado!')
        return render(request, 'accounts/cadastroMonitor.html', {'form': form})

    if User.objects.filter(email=email_instituicao).exists():
        messages.error(request, 'Email institucional ja cadastrado!')
        return render(request, 'accounts/cadastroMonitor.html', {'form': form})

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais!')
        return render(request, 'accounts/cadastroAluno.html',  {'form': form})

    if senha != senha2:
        messages.error(request, 'Senhas diferentes, tente novamente!')
        return render(request, 'accounts/cadastroMonitor.html')

    messages.success(request, 'Cadastro com sucesso, realize seu primeiro Login!')

    user = User.objects.create_user(username=usuario, email=email_pessoal,
                                    password=senha, first_name=nome,
                                    last_name=email_instituicao)
    form.save()
    user.save()
    return redirect('login')

def cadastroTutor(request):
    if request.method != 'POST':
        form = FormTutor()
        return render(request, 'accounts/cadastroTutor.html', {'form': form})

    form = FormTutor(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar suas informacoes, tente novamente!')
        form = FormTutor(request.POST)
        return render(request, 'accounts/cadastroTutor.html', {'form': form})


    nome = request.POST.get('tut_nome')
    usuario = request.POST.get('tut_cpf')
    sexo = request.POST.get('tut_genero')
    email_pessoal = request.POST.get('tut_email_pessoal')
    email_instituicao = request.POST.get('tut_email_institucional')
    telefone = request.POST.get('tut_telefone')
    cep = request.POST.get('tut_endereco_cep')
    descricao_des = request.POST.get('tut_endereco_descricao')
    cidade = request.POST.get('tut_endereco_cidade')
    curso = request.POST.get(' tut_curso')
    periodo = request.POST.get('tut_periodo_academico')
    matricula = request.POST.get('tut_matricula')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not usuario or not sexo or not email_pessoal or not email_instituicao or not telefone or not cep or not descricao_des or not cidade or not periodo or not matricula or not senha or not senha2:
        messages.error(request, 'Todos os campos devem ser preenchidos!')
        return render(request, 'accounts/cadastroTutor.html', {'form': form})

    try:
        validate_email(email_pessoal)
    except:
        messages.error(request, 'Email pessoal invalido!')
        return render(request, 'accounts/cadastroTutor.html', {'form': form})

    try:
        validate_email(email_instituicao)
    except:
        messages.error(request, 'Email institucional invalido!')
        return render(request, 'accounts/cadastroTutor.html', {'form': form})

    try:
         valida_cpf(usuario)
    except:
        messages.error(request, 'Cpf nao é valido!')
        return render(request, 'accounts/cadastroTutor.html', {'form': form})

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Cpf ja cadastrado, verifique e tente novamente!')
        return render(request, 'accounts/cadastroTutor.html', {'form': form})

    if User.objects.filter(email=email_pessoal).exists():
        messages.error(request, 'Email pessoal ja cadastrado!')
        return render(request, 'accounts/cadastroTutor.html', {'form': form})

    if User.objects.filter(email=email_instituicao).exists():
        messages.error(request, 'Email institucional ja cadastrado!')
        return render(request, 'accounts/cadastroTutor.html', {'form': form})

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/cadastroTutor.html', {'form': form})

    if senha != senha2:
        messages.error(request, 'Senhas diferentes, tente novamente!')
        return render(request, 'accounts/cadastroTutor.html')


    messages.success(request, 'Cadastro com sucesso, realize seu primeiro Login!')

    user = User.objects.create_user(username=usuario, email=email_pessoal,
                                    password=senha, first_name=nome,
                                    last_name=email_instituicao)
    form.save()
    user.save()
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboardAluno(request):
    if request.method != 'POST':
        form = FormAlunoPcd()
        return render(request, 'accounts/dashboardAluno.html', {'form': form})

    form = FormAlunoPcd(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar suas informacoes')
        form = FormAlunoPcd(request.POST)
        return render(request, 'accounts/dashboardAluno.html', {'form': form})


    form.save()
    messages.success(request, f'Usuario {request.POST.get("adm_nome")} salvo com sucesso!')
    return redirect('dashboard')



def valida_cpf(f):
    cpf = f
    novo_cpf = cpf[:-2]  # Elimina os dois últimos digitos do CPF
    reverso = 10  # Contador reverso
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:  # Primeiro índice vai de 0 a 9,
            index -= 9  # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1  # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:  # Se o digito for > que 9 o valor é 0
                d = 0
            total = 0  # Zera o total
            novo_cpf += str(d)  # Concatena o digito gerado no novo cpf

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # Descobri que sequências avaliavam como verdadeiro, então também
    # adicionei essa checagem aqui
    if cpf == novo_cpf and not sequencia:
        return True
    else:
        return False

def valida_string(s):
    validos = ascii_letters + ' áàâãéèêíïóôõöúçñ'
    while True:

        if all(c in validos for c in s):
            break  # sai do while
        else:
            return False