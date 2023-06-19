import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.views.generic.list import ListView
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.validators import validate_email
from django.contrib import messages
from .models import AlunoPcd, Monitor, Tutor, Interprete, Administrador, CustomUser
from .forms import AlunosForm, MonitoresForm, TutoresForm, InterpretesForm, AdminsForm, AtualizarAlunosForm, AtualizarMonitoresForm, AtualizarTutoresForm, AtualizarInterpretesForm
from authentication.views import valida_cpf, valida_string
from acompanhamentos.models import Acompanhamentos
from feedbacks.forms import FeedbacksForm
from feedbacks.models import Feedbacks
from PIL import Image

# Create your views here.
#ADMIN================================================================================================

def admIndex(request):
    return render(request, 'administrador/admIndex.html')

def homologarAtivo(request):
    alunos = AlunoPcd.objects.all().order_by('alu_nome').filter(alu_ativo = True)
    monitores = Monitor.objects.all().order_by('mon_nome').filter(mon_ativo = True)
    tutores = Tutor.objects.all().order_by('tut_nome').filter(tut_ativo = True)
    interpretes = Interprete.objects.all().order_by('int_nome').filter(int_ativo = True)

    return render(request, 'administrador/homologarAtivo.html', {
        'alunos': alunos,
        'monitores': monitores,
        'tutores': tutores,
        'interpretes': interpretes
    })

def homologarInativo(request):
    alunos = AlunoPcd.objects.all().order_by('alu_nome').filter(alu_ativo = False)
    monitores = Monitor.objects.all().order_by('mon_nome').filter(mon_ativo = False)
    tutores = Tutor.objects.all().order_by('tut_nome').filter(tut_ativo = False)
    interpretes = Interprete.objects.all().order_by('int_nome').filter(int_ativo = False)

    return render(request, 'administrador/homologarInativo.html', {
        'alunos': alunos,
        'monitores': monitores,
        'tutores': tutores,
        'interpretes': interpretes
    })

def ativarAluno(request, aluno_id):
    usuario = get_object_or_404(AlunoPcd, alu_id=aluno_id)
    usuario.ativar(request)
    return redirect('homologarInativo')

def ativarMonitor(request, monitor_id):
    usuario = get_object_or_404(Monitor, mon_id=monitor_id)
    usuario.ativar(request)
    return redirect('homologarInativo')

def ativarTutor(request, tutor_id):
    usuario = get_object_or_404(Tutor, tut_id=tutor_id)
    usuario.ativar(request)
    return redirect('homologarInativo')

def ativarInterprete(request, interprete_id):
    usuario = get_object_or_404(Interprete, int_id=interprete_id)
    usuario.ativar(request)
    return redirect('homologarInativo')
def desativarAluno(request, aluno_id):
    usuario = get_object_or_404(AlunoPcd, alu_id=aluno_id)
    usuario.desativar(request)
    return redirect('homologarAtivo')

def desativarMonitor(request, monitor_id):
    usuario = get_object_or_404(Monitor, mon_id=monitor_id)
    usuario.desativar(request)
    return redirect('homologarAtivo')

def desativarTutor(request, tutor_id):
    usuario = get_object_or_404(Tutor, tut_id=tutor_id)
    usuario.desativar(request)
    return redirect('homologarAtivo')

def desativarInterprete(request, interprete_id):
    usuario = get_object_or_404(Interprete, int_id=interprete_id)
    usuario.desativar(request)
    return redirect('homologarAtivo')

def homologarAlunoAtivo(request, aluno_id):
    aluno = get_object_or_404(AlunoPcd, alu_id=aluno_id)

    return render(request, 'administrador/homologarAlunoAtivo.html', {
        'aluno': aluno
    })

def homologarAlunoInativo(request, aluno_id):
    aluno = get_object_or_404(AlunoPcd, alu_id=aluno_id)

    return render(request, 'administrador/homologarAlunoInativo.html', {
        'aluno': aluno
    })

def homologarInterpreteAtivo(request, interprete_id):
    interprete = get_object_or_404(Interprete, int_id=interprete_id)

    return render(request, 'administrador/homologarInterpreteAtivo.html', {
        'interprete': interprete
    })

def homologarInterpreteInativo(request, interprete_id):
    interprete = get_object_or_404(Interprete, int_id=interprete_id)

    return render(request, 'administrador/homologarInterpreteInativo.html', {
        'interprete': interprete
    })

def homologarMonitorAtivo(request, monitor_id):
    monitor = get_object_or_404(Monitor, mon_id=monitor_id)

    return render(request, 'administrador/homologarMonitorAtivo.html', {
        'monitor': monitor
    })

def homologarMonitorInativo(request, monitor_id):
    monitor = get_object_or_404(Monitor, mon_id=monitor_id)

    return render(request, 'administrador/homologarMonitorInativo.html', {
        'monitor': monitor
    })

def homologarTutorAtivo(request, tutor_id):
    tutor = get_object_or_404(Tutor, tut_id=tutor_id)

    return render(request, 'administrador/homologarTutorAtivo.html', {
        'tutor': tutor
    })

def homologarTutorInativo(request, tutor_id):
    tutor = get_object_or_404(Tutor, tut_id=tutor_id)

    return render(request, 'administrador/homologarTutorInativo.html', {
        'tutor': tutor
    })

def buscarAtivo(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            try:
                alunos = AlunoPcd.objects.order_by('alu_nome').filter(
                    Q(alu_nome__icontains=searched) | Q(alu_curso__icontains=searched)).filter(alu_ativo=True)
                monitores = Monitor.objects.order_by('mon_nome').filter(
                    Q(mon_nome__icontains=searched)).filter(mon_ativo=True)
                tutores = Tutor.objects.order_by('tut_nome').filter(
                    Q(tut_nome__icontains=searched)).filter(tut_ativo=True)
                interpretes = Interprete.objects.order_by('int_nome').filter(
                    Q(int_nome__icontains=searched)).filter(int_ativo=True)
            except:
                alunos = AlunoPcd.objects.order_by('alu_nome').filter(
                    Q(alu_nome__icontains=searched)).filter(alu_ativo=True)
                monitores = Monitor.objects.order_by('mon_nome').filter(
                    Q(mon_nome__icontains=searched)).filter(mon_ativo=True)
                tutores = Tutor.objects.order_by('tut_nome').filter(
                    Q(tut_nome__icontains=searched)).filter(tut_ativo=True)
                interpretes = Interprete.objects.order_by('int_nome').filter(
                    Q(int_nome__icontains=searched)).filter(int_ativo=True)
        else:
            alunos = None
            monitores = None
            tutores = None
            interpretes = None

        return render(request, 'administrador/buscarAtivo.html', {
            'searched': searched,
            'alunos': alunos,
            'monitores': monitores,
            'tutores': tutores,
            'interpretes': interpretes
        })
    else:
        return render(request, 'administrador/buscarAtivo.html', {

        })

def buscarInativo(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            try:
                alunos = AlunoPcd.objects.order_by('alu_nome').filter(
                    Q(alu_nome__icontains=searched) | Q(alu_curso__icontains=searched)).filter(alu_ativo=False)
                monitores = Monitor.objects.order_by('mon_nome').filter(
                    Q(mon_nome__icontains=searched)).filter(mon_ativo=False)
                tutores = Tutor.objects.order_by('tut_nome').filter(
                    Q(tut_nome__icontains=searched)).filter(tut_ativo=False)
                interpretes = Interprete.objects.order_by('int_nome').filter(
                    Q(int_nome__icontains=searched)).filter(int_ativo=False)
            except:
                alunos = AlunoPcd.objects.order_by('alu_nome').filter(
                    Q(alu_nome__icontains=searched)).filter(alu_ativo=False)
                monitores = Monitor.objects.order_by('mon_nome').filter(
                    Q(mon_nome__icontains=searched)).filter(mon_ativo=False)
                tutores = Tutor.objects.order_by('tut_nome').filter(
                    Q(tut_nome__icontains=searched)).filter(tut_ativo=False)
                interpretes = Interprete.objects.order_by('int_nome').filter(
                    Q(int_nome__icontains=searched)).filter(int_ativo=False)
        else:
            alunos = None
            monitores = None
            tutores = None
            interpretes = None

        return render(request, 'administrador/buscarInativo.html', {
            'searched': searched,
            'alunos': alunos,
            'monitores': monitores,
            'tutores': tutores,
            'interpretes': interpretes
        })
    else:
        return render(request, 'administrador/buscarInativo.html', {

        })

def deletarAlunoAtivo(request, aluno_id):
    aluno = get_object_or_404(AlunoPcd, alu_id=aluno_id)
    aluno.delete()
    return redirect('homologarAtivo')

def deletarAlunoInativo(request, aluno_id):
    aluno = get_object_or_404(AlunoPcd, alu_id=aluno_id)
    aluno.delete()
    return redirect('homologarInativo')

def deletarMonitorAtivo(request, monitor_id):
    monitor = get_object_or_404(Monitor, mon_id=monitor_id)
    monitor.delete()
    return redirect('homologarAtivo')

def deletarMonitorInativo(request, monitor_id):
    monitor = get_object_or_404(Monitor, mon_id=monitor_id)
    monitor.delete()
    return redirect('homologarInativo')

def deletarTutorAtivo(request, tutor_id):
    tutor = get_object_or_404(Tutor, tut_id=tutor_id)
    tutor.delete()
    return redirect('homologarAtivo')

def deletarTutorInativo(request, tutor_id):
    tutor = get_object_or_404(Tutor, tut_id=tutor_id)
    tutor.delete()
    return redirect('homologarInativo')

def deletarInterpreteAtivo(request, interprete_id):
    interprete = get_object_or_404(Interprete, int_id=interprete_id)
    interprete.delete()
    return redirect('homologarAtivo')

def deletarInterpreteInativo(request, interprete_id):
    interprete = get_object_or_404(Interprete, int_id=interprete_id)
    interprete.delete()
    return redirect('homologarInativo')

def administradores(request):
    administradores = Administrador.objects.all().order_by('adm_nome')

    paginator = Paginator(administradores, 10)
    page = request.GET.get('p')
    administradores = paginator.get_page(page)

    return render(request, 'administrador/administradores.html', {
        'administradores': administradores
    })

def adicionarAdmin(request):
    if request.method == "POST":
        form = AdminsForm(request.POST, request.FILES)
        if form.is_valid():
            nome = request.POST.get('adm_nome')
            usuario = request.POST.get('adm_cpf')
            email = request.POST.get('adm_email')
            senha = request.POST.get('senha')
            senha2 = request.POST.get('senha2')
            permissao = 1

            if not nome or not usuario or not email or not senha or not senha2:
                messages.error(request, 'Todos os campos devem ser preenchidos!')
                return render(request, 'administrador/adicionarAdmin.html', {'form': form})

            try:
                valida_string(nome)
            except:
                messages.error(request, 'Por favor digite somente letras e espaços')
                return render(request, 'administrador/adicionarAdmin.html', {'form': form})

            try:
                validate_email(email)
            except:
                messages.error(request, 'Email pessoal invalido!')
                return render(request, 'administrador/adicionarAdmin.html', {'form': form})

            try:
                valida_cpf(usuario)
            except:
                messages.error(request, 'O Cpf informado não é valido, tente novamente!')
                return render(request, 'administrador/adicionarAdmin.html', {'form': form})

            if CustomUser.objects.filter(username=usuario).exists():
                messages.error(request, 'Cpf já cadastrado, verifique e tente novamente!')
                return render(request, 'administrador/adicionarAdmin.html', {'form': form})

            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Email já cadastrado, tente novamente!')
                return render(request, 'administrador/adicionarAdmin.html', {'form': form})

            if len(senha) < 6:
                messages.error(request, 'Senha precisa ter 7 caracteres ou mais.')
                return render(request, 'administrador/adicionarAdmin.html', {'form': form})

            if senha != senha2:
                messages.error(request, 'Senhas diferentes, tente novamente!')
                return render(request, 'administrador/adicionarAdmin.html')

            user = CustomUser.objects.create_user(username=usuario, email=email, user_type=permissao, password=senha)
            if user is not None:
                userForm = form.save(commit=False)
                userForm.adm_usuario = user
                userForm.save()
                user.is_active = True
                user.save()
                messages.success(request, '''Cadastro de usuário admin realizado com sucesso!''')
                return redirect("administradores")
            else:
                messages.error("ocorreu um erro na tentativa de cadastro! Usuário não foi criado.")
                return redirect("administradores")
        else:
            messages.error(request, 'Informações invalidas, tente novamente!')
            form = AdminsForm(request.POST)
    else:
        form = AdminsForm()

    return render(request, 'administrador/adicionarAdmin.html', {
        'form': form,
    })

def buscarAdmin(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            try:
                administradores = Administrador.objects.order_by('adm_nome').filter(Q(adm_nome__icontains=searched) | Q(adm_email__icontains=searched))
            except:
                administradores = Administrador.objects.order_by('adm_nome').filter(Q(adm_nome__icontains=searched))
        else:
            administradores = None

        return render(request, 'administrador/buscarAdmin.html', {
            'searched': searched,
            'administradores': administradores
        })
    else:
        return render(request, 'administrador/buscarAdmin.html', {

        })

def deletarAdmin(request, admin_id):
    administrador = get_object_or_404(Administrador, adm_id=admin_id)
    administrador.delete()
    return redirect('administradores')

def adminAlunos(request):
    alunos = AlunoPcd.objects.all().order_by('alu_nome')


    paginator = Paginator(alunos, 10)
    page = request.GET.get('p')
    alunos = paginator.get_page(page)

    return render(request, 'administrador/alunos.html', {
        'alunos': alunos
    })

def adicionarAluno(request):
    if request.method == "POST":
        form = AlunosForm(request.POST, request.FILES)
        if form.is_valid():
            nome = request.POST.get('alu_nome')
            usuario = request.POST.get('alu_cpf')
            data_nascimento = request.POST.get('alu_data_nascimento')
            genero = request.POST.get('alu_genero')
            email_pessoal = request.POST.get('alu_email_pessoal')
            email_instituicao = request.POST.get('alu_email_institucional')
            telefone = request.POST.get('alu_telefone')
            cep = request.POST.get('alu_endereco_cep')
            endereco_des = request.POST.get('alu_endereco_descricao')
            cidade = request.POST.get('alu_endereco_cidade')
            curso = request.POST.get('alu_curso')
            periodo = request.POST.get('alu_periodo_academico')
            matricula = request.POST.get('alu_matricula')
            deficiencias = request.POST.get('alu_deficiencias')
            senha = request.POST.get('senha')
            senha2 = request.POST.get('senha2')
            permissao = 2

            if not nome or not usuario or not data_nascimento or not genero or not email_pessoal or not email_instituicao or not telefone or not cep or not endereco_des or not cidade or not curso or not periodo or not matricula or not senha or not senha2:
                messages.error(request, 'Todos os campos devem ser preenchidos!')
                return render(request, 'administrador/adicionarAluno.html', {'form': form})

            try:
                valida_string(nome)
            except:
                messages.error(request, 'Por favor digite somente letras e espaços')
                return render(request, 'administrador/adicionarAluno.html', {'form': form})

            try:
                validate_email(email_pessoal)
            except:
                messages.error(request, 'Email pessoal invalido!')
                return render(request, 'administrador/adicionarAluno.html', {'form': form})

            try:
                validate_email(email_instituicao)
            except:
                messages.error(request, 'Email institucional invalido!')
                return render(request, 'administrador/adicionarAluno.html', {'form': form})

            try:
                valida_cpf(usuario)
            except:
                messages.error(request, 'O Cpf informado não é valido, tente novamente!')
                return render(request, 'administrador/adicionarAluno.html', {'form': form})

            if CustomUser.objects.filter(username=usuario).exists():
                messages.error(request, 'Cpf já cadastrado, verifique e tente novamente!')
                return render(request, 'administrador/adicionarAluno.html', {'form': form})

            if CustomUser.objects.filter(email=email_pessoal).exists():
                messages.error(request, 'Email pessoal já cadastrado, tente novamente!')
                return render(request, 'administrador/adicionarAluno.html', {'form': form})

            if CustomUser.objects.filter(email=email_instituicao).exists():
                messages.error(request, 'Email institucional já cadastrado, tente novamente!')
                return render(request, 'administrador/adicionarAluno.html', {'form': form})

            if len(senha) < 6:
                messages.error(request, 'Senha precisa ter 7 caracteres ou mais.')
                return render(request, 'administrador/adicionarAluno.html', {'form': form})

            if senha != senha2:
                messages.error(request, 'Senhas diferentes, tente novamente!')
                return render(request, 'administrador/adicionarAluno.html')

            user = CustomUser.objects.create_user(username=usuario, email=email_instituicao,
                                                  password=senha, user_type=permissao)
            if user is not None:
                userForm = form.save(commit=False)
                userForm.alu_usuario = user
                userForm.alu_ativo = True
                userForm.save()
                user.is_active = True
                user.save()
                messages.success(request, '''Cadastro de usuário aluno realizado com sucesso!''')
                return redirect("alunos")
            else:
                messages.error("ocorreu um erro na tentativa de cadastro! Usuário não foi criado.")
                return redirect("alunos")
        else:
            messages.error(request, 'Informações invalidas, tente novamente!')
            form = AlunosForm(request.POST)
    else:
        form = AlunosForm()

    return render(request, 'administrador/adicionarAluno.html', {
        'form': form,
    })

def buscarAluno(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            try:
                alunos = AlunoPcd.objects.order_by('alu_nome').filter(
                    Q(alu_nome__icontains=searched) |
                    Q(alu_curso__icontains=searched) |
                    Q(alu_email_institucional__icontains=searched) |
                    Q(alu_email_pessoal__icontains=searched)
                )
            except:
                alunos = AlunoPcd.objects.order_by('alu_nome').filter(Q(alu_nome__icontains=searched))
        else:
            alunos = None

        return render(request, 'administrador/buscarAluno.html', {
            'searched': searched,
            'alunos': alunos
        })
    else:
        return render(request, 'administrador/buscarAluno.html', {

        })


def admAluno(request, aluno_id):
    aluno = get_object_or_404(AlunoPcd, alu_id=aluno_id)

    return render(request, 'administrador/admAluno.html', {
        'aluno': aluno
    })

def atualizarAluno(request, aluno_id):
    aluno = get_object_or_404(AlunoPcd, alu_id=aluno_id)

    form = AtualizarAlunosForm(request.POST or None, instance=aluno)
    if form.is_valid():
        form.save()
        return redirect('alunos')

    return render(request, 'administrador/atualizarAluno.html', {
        'aluno': aluno,
        'form': form
    })

def deletarAluno(request, aluno_id):
    aluno = get_object_or_404(AlunoPcd, alu_id=aluno_id)
    aluno.delete()
    return redirect('alunos')

def adminMonitores(request):
    monitores = Monitor.objects.all().order_by('mon_nome')

    paginator = Paginator(monitores, 10)
    page = request.GET.get('p')
    monitores = paginator.get_page(page)

    return render(request, 'administrador/monitores.html', {
        'monitores': monitores
    })


def adicionarMonitor(request):
    if request.method == "POST":
        form = MonitoresForm(request.POST, request.FILES)
        if form.is_valid():
            nome = request.POST.get('mon_nome')
            usuario = request.POST.get('mon_cpf')
            genero = request.POST.get('mon_genero')
            email_pessoal = request.POST.get('mon_email_pessoal')
            email_instituicao = request.POST.get('mon_email_institucional')
            telefone = request.POST.get('mon_telefone')
            cep = request.POST.get('mon_endereco_cep')
            endereco_des = request.POST.get('mon_endereco_descricao')
            cidade = request.POST.get('mon_endereco_cidade')
            curso = request.POST.get('mon_curso')
            periodo = request.POST.get('mon_periodo_academico')
            matricula = request.POST.get('mon_matricula')
            senha = request.POST.get('senha')
            senha2 = request.POST.get('senha2')
            permissao = 3

            if not nome or not usuario or not genero or not email_pessoal or not email_instituicao or not telefone or not cep or not endereco_des or not cidade or not curso or not periodo or not matricula or not senha or not senha2:
                messages.error(request, 'Todos os campos devem ser preenchidos!')
                return render(request, 'administrador/adicionarMonitor.html', {'form': form})

            try:
                valida_string(nome)
            except:
                messages.error(request, 'Por favor digite somente letras e espaços')
                return render(request, 'administrador/adicionarMonitor.html', {'form': form})

            try:
                validate_email(email_pessoal)
            except:
                messages.error(request, 'Email pessoal invalido!')
                return render(request, 'administrador/adicionarMonitor.html', {'form': form})

            try:
                validate_email(email_instituicao)
            except:
                messages.error(request, 'Email institucional invalido!')
                return render(request, 'administrador/adicionarMonitor.html', {'form': form})

            try:
                valida_cpf(usuario)
            except:
                messages.error(request, 'O Cpf informado não é valido, tente novamente!')
                return render(request, 'administrador/adicionarMonitor.html', {'form': form})

            if CustomUser.objects.filter(username=usuario).exists():
                messages.error(request, 'Cpf já cadastrado, verifique e tente novamente!')
                return render(request, 'administrador/adicionarMonitor.html', {'form': form})

            if CustomUser.objects.filter(email=email_pessoal).exists():
                messages.error(request, 'Email pessoal já cadastrado, tente novamente!')
                return render(request, 'administrador/adicionarMonitor.html', {'form': form})

            if CustomUser.objects.filter(email=email_instituicao).exists():
                messages.error(request, 'Email institucional já cadastrado, tente novamente!')
                return render(request, 'administrador/adicionarMonitor.html', {'form': form})

            if len(senha) < 6:
                messages.error(request, 'Senha precisa ter 7 caracteres ou mais.')
                return render(request, 'administrador/adicionarMonitor.html', {'form': form})

            if senha != senha2:
                messages.error(request, 'Senhas diferentes, tente novamente!')
                return render(request, 'administrador/adicionarMonitor.html')

            user = CustomUser.objects.create_user(username=usuario, email=email_instituicao,
                                                  password=senha, user_type=permissao)

            if user is not None:
                userForm = form.save(commit=False)
                userForm.mon_usuario = user
                userForm.mon_ativo = True
                userForm.save()
                user.is_active = True
                user.save()
                messages.success(request, '''Cadastro de usuário monitor realizado com sucesso!''')
                return redirect("monitores")
            else:
                messages.error("ocorreu um erro na tentativa de cadastro! Usuário não foi criado.")
                return redirect("monitores")
        else:
            messages.error(request, 'Informações invalidas, tente novamente!')
            form = MonitoresForm(request.POST)
    else:
        form = MonitoresForm()

    return render(request, 'administrador/adicionarMonitor.html', {
        'form': form,
    })


def buscarMonitor(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            try:
                monitores = Monitor.objects.order_by('mon_nome').filter(
                    Q(mon_nome__icontains=searched) |
                    Q(mon_curso__icontains=searched) |
                    Q(mon_email_institucional__icontains=searched) |
                    Q(mon_email_pessoal__icontains=searched)
                )
            except:
                monitores = Monitor.objects.order_by('mon_nome').filter(Q(mon_nome__icontains=searched))
        else:
            monitores = None

        return render(request, 'administrador/buscarMonitor.html', {
            'searched': searched,
            'monitores': monitores
        })
    else:
        return render(request, 'administrador/buscarMonitor.html', {

        })


def admMonitor(request, monitor_id):
    monitor = get_object_or_404(Monitor, mon_id=monitor_id)

    return render(request, 'administrador/admMonitor.html', {
        'monitor': monitor
    })


def atualizarMonitor(request, monitor_id):
    monitor = get_object_or_404(Monitor, mon_id=monitor_id)

    form = AtualizarMonitoresForm(request.POST or None, instance=monitor)
    if form.is_valid():
        form.save()
        return redirect('monitores')

    return render(request, 'administrador/atualizarMonitor.html', {
        'monitor': monitor,
        'form': form
    })


def deletarMonitor(request, monitor_id):
    monitor = get_object_or_404(Monitor, mon_id=monitor_id)
    monitor.delete()
    return redirect('monitores')

def adminTutores(request):
    tutores = Tutor.objects.all().order_by('tut_nome')

    paginator = Paginator(tutores, 10)
    page = request.GET.get('p')
    tutores = paginator.get_page(page)

    return render(request, 'administrador/tutores.html', {
        'tutores': tutores
    })


def adicionarTutor(request):
    if request.method == "POST":
        form = TutoresForm(request.POST, request.FILES)
        if form.is_valid():
            nome = request.POST.get('tut_nome')
            usuario = request.POST.get('tut_cpf')
            genero = request.POST.get('tut_genero')
            email_pessoal = request.POST.get('tut_email_pessoal')
            email_instituicao = request.POST.get('tut_email_institucional')
            telefone = request.POST.get('tut_telefone')
            cep = request.POST.get('tut_endereco_cep')
            endereco_des = request.POST.get('tut_endereco_descricao')
            cidade = request.POST.get('tut_endereco_cidade')
            curso = request.POST.get('tut_curso')
            periodo = request.POST.get('tut_periodo_academico')
            matricula = request.POST.get('tut_matricula')
            senha = request.POST.get('senha')
            senha2 = request.POST.get('senha2')
            permissao = 4

            if not nome or not usuario or not genero or not email_pessoal or not email_instituicao or not telefone or not cep or not endereco_des or not cidade or not curso or not periodo or not matricula or not senha or not senha2:
                messages.error(request, 'Todos os campos devem ser preenchidos!')
                return render(request, 'administrador/adicionarTutor.html', {'form': form})

            try:
                valida_string(nome)
            except:
                messages.error(request, 'Por favor digite somente letras e espaços')
                return render(request, 'administrador/adicionarTutor.html', {'form': form})

            try:
                validate_email(email_pessoal)
            except:
                messages.error(request, 'Email pessoal invalido!')
                return render(request, 'administrador/adicionarTutor.html', {'form': form})

            try:
                validate_email(email_instituicao)
            except:
                messages.error(request, 'Email institucional invalido!')
                return render(request, 'administrador/adicionarTutor.html', {'form': form})

            try:
                valida_cpf(usuario)
            except:
                messages.error(request, 'O Cpf informado não é valido, tente novamente!')
                return render(request, 'administrador/adicionarTutor.html', {'form': form})

            if CustomUser.objects.filter(username=usuario).exists():
                messages.error(request, 'Cpf já cadastrado, verifique e tente novamente!')
                return render(request, 'administrador/adicionarTutor.html', {'form': form})

            if CustomUser.objects.filter(email=email_pessoal).exists():
                messages.error(request, 'Email pessoal já cadastrado, tente novamente!')
                return render(request, 'administrador/adicionarTutor.html', {'form': form})

            if CustomUser.objects.filter(email=email_instituicao).exists():
                messages.error(request, 'Email institucional já cadastrado, tente novamente!')
                return render(request, 'administrador/adicionarTutor.html', {'form': form})

            if len(senha) < 6:
                messages.error(request, 'Senha precisa ter 7 caracteres ou mais.')
                return render(request, 'administrador/adicionarTutor.html', {'form': form})

            if senha != senha2:
                messages.error(request, 'Senhas diferentes, tente novamente!')
                return render(request, 'administrador/adicionarTutor.html')

            user = CustomUser.objects.create_user(username=usuario, email=email_instituicao,
                                                  password=senha, user_type=permissao)

            if user is not None:
                userForm = form.save(commit=False)
                userForm.tut_usuario = user
                userForm.tut_ativo = True
                userForm.save()
                user.is_active = True
                user.save()
                messages.success(request, '''Cadastro de usuário tutor realizado com sucesso!''')
                return redirect("tutores")
            else:
                messages.error("ocorreu um erro na tentativa de cadastro! Usuário não foi criado.")
                return redirect("tutores")
        else:
            messages.error(request, 'Informações invalidas, tente novamente!')
            form = TutoresForm(request.POST)
    else:
        form = TutoresForm()

    return render(request, 'administrador/adicionarTutor.html', {
        'form': form,
    })


def buscarTutor(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            try:
                tutores = Tutor.objects.order_by('tut_nome').filter(
                    Q(tut_nome__icontains=searched) |
                    Q(tut_curso__icontains=searched) |
                    Q(tut_email_institucional__icontains=searched) |
                    Q(tut_email_pessoal__icontains=searched)
                )
            except:
                tutores = Tutor.objects.order_by('tut_nome').filter(Q(tut_nome__icontains=searched))
        else:
            tutores = None

        return render(request, 'administrador/buscarTutor.html', {
            'searched': searched,
            'tutores': tutores
        })
    else:
        return render(request, 'administrador/buscarTutor.html', {

        })


def admTutor(request, tutor_id):
    tutor = get_object_or_404(Tutor, tut_id=tutor_id)

    return render(request, 'administrador/admTutor.html', {
        'tutor': tutor
    })


def atualizarTutor(request, tutor_id):
    tutor = get_object_or_404(Tutor, tut_id=tutor_id)

    form = AtualizarTutoresForm(request.POST or None, instance=tutor)
    if form.is_valid():
        form.save()
        return redirect('tutores')

    return render(request, 'administrador/atualizarTutor.html', {
        'tutor': tutor,
        'form': form
    })


def deletarTutor(request, tutor_id):
    tutor = get_object_or_404(Tutor, tut_id=tutor_id)
    tutor.delete()
    return redirect('tutores')

def adminInterpretes(request):
    interpretes = Interprete.objects.all().order_by('int_nome')

    paginator = Paginator(interpretes, 10)
    page = request.GET.get('p')
    interpretes = paginator.get_page(page)

    return render(request, 'administrador/interpretes.html', {
        'interpretes': interpretes
    })


def adicionarInterprete(request):
    if request.method == "POST":
        form = InterpretesForm(request.POST, request.FILES)
        if form.is_valid():
            nome = request.POST.get('int_nome')
            usuario = request.POST.get('int_cpf')
            genero = request.POST.get('int_genero')
            email_pessoal = request.POST.get('int_email_pessoal')
            email_instituicao = request.POST.get('int_email_institucional')
            telefone = request.POST.get('int_telefone')
            senha = request.POST.get('senha')
            senha2 = request.POST.get('senha2')
            permissao = 5

            if not nome or not usuario or not genero or not email_pessoal or not email_instituicao or not telefone or not senha or not senha2:
                messages.error(request, 'Todos os campos devem ser preenchidos!')
                return render(request, 'administrador/adicionarInterprete.html', {'form': form})

            try:
                valida_string(nome)
            except:
                messages.error(request, 'Por favor digite somente letras e espaços')
                return render(request, 'administrador/adicionarInterprete.html', {'form': form})

            try:
                validate_email(email_pessoal)
            except:
                messages.error(request, 'Email pessoal invalido!')
                return render(request, 'administrador/adicionarInterprete.html', {'form': form})

            try:
                validate_email(email_instituicao)
            except:
                messages.error(request, 'Email institucional invalido!')
                return render(request, 'administrador/adicionarInterprete.html', {'form': form})

            try:
                valida_cpf(usuario)
            except:
                messages.error(request, 'O Cpf informado não é valido, tente novamente!')
                return render(request, 'administrador/adicionarInterprete.html', {'form': form})

            if CustomUser.objects.filter(username=usuario).exists():
                messages.error(request, 'Cpf já cadastrado, verifique e tente novamente!')
                return render(request, 'administrador/adicionarInterprete.html', {'form': form})

            if CustomUser.objects.filter(email=email_pessoal).exists():
                messages.error(request, 'Email pessoal já cadastrado, tente novamente!')
                return render(request, 'administrador/adicionarInterprete.html', {'form': form})

            if CustomUser.objects.filter(email=email_instituicao).exists():
                messages.error(request, 'Email institucional já cadastrado, tente novamente!')
                return render(request, 'administrador/adicionarInterprete.html', {'form': form})

            if len(senha) < 6:
                messages.error(request, 'Senha precisa ter 7 caracteres ou mais.')
                return render(request, 'administrador/adicionarInterprete.html', {'form': form})

            if senha != senha2:
                messages.error(request, 'Senhas diferentes, tente novamente!')
                return render(request, 'administrador/adicionarInterprete.html')

            user = CustomUser.objects.create_user(username=usuario, email=email_instituicao,
                                                  password=senha, user_type=permissao)
            if user is not None:
                userForm = form.save(commit=False)
                userForm.int_ativo = True
                userForm.int_usuario = user
                userForm.save()
                user.is_active = True
                user.save()
                messages.success(request, '''Cadastro de usuário interprete realizado com sucesso!''')
                return redirect("interpretes")
            else:
                messages.error("ocorreu um erro na tentativa de cadastro! Usuário não foi criado.")
                return redirect("interpretes")
        else:
            messages.error(request, 'Informações invalidas, tente novamente!')
            form = InterpretesForm(request.POST)
    else:
        form = InterpretesForm()

    return render(request, 'administrador/adicionarInterprete.html', {
        'form': form,
    })


def buscarInterprete(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            try:
                interpretes = Interprete.objects.order_by('int_nome').filter(
                    Q(int_nome__icontains=searched) |
                    Q(int_email_institucional__icontains=searched) |
                    Q(int_email_pessoal__icontains=searched)
                )
            except:
                interpretes = Interprete.objects.order_by('int_nome').filter(Q(int_nome__icontains=searched))
        else:
            interpretes = None

        return render(request, 'administrador/buscarInterprete.html', {
            'searched': searched,
            'interpretes': interpretes
        })
    else:
        return render(request, 'administrador/buscarInterprete.html', {

        })


def admInterprete(request, interprete_id):
    interprete = get_object_or_404(Interprete, int_id=interprete_id)

    return render(request, 'administrador/admInterprete.html', {
        'interprete': interprete
    })


def atualizarInterprete(request, interprete_id):
    interprete = get_object_or_404(Interprete, int_id=interprete_id)

    form = AtualizarInterpretesForm(request.POST or None, instance=interprete)
    if form.is_valid():
        form.save()
        return redirect('interpretes')

    return render(request, 'administrador/atualizarInterprete.html', {
        'interprete': interprete,
        'form': form
    })


def deletarInterprete(request, interprete_id):
    interprete = get_object_or_404(Interprete, int_id=interprete_id)
    interprete.delete()
    return redirect('interpretes')

#ALUNO================================================================================================

def aluIndex(request):
    alunos = AlunoPcd.objects.all()
    paginator = Paginator(alunos, 10)

    page = request.GET.get('p')
    alunos = paginator.get_page(page)

    return render(request, 'alunos/aluIndex.html', {
     'alunos' : alunos
    })

def acompanhantes(request):
    return render(request, 'alunos/acompanhantes.html')

def aluno(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    aluno = get_object_or_404(AlunoPcd, alu_usuario=user)
    return render(request, 'alunos/aluno.html', {
        'aluno' : aluno
    })

def atualizarAlunoPerfil(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    aluno = get_object_or_404(AlunoPcd, alu_cpf=user.username)

    form = AtualizarAlunosForm(request.POST or None, instance=aluno)
    if form.is_valid():
        form.save()
        messages.success(request, 'Perfil alterado com sucesso!')
        return redirect('aluno', user.id)

    return render(request, 'alunos/atualizarAlunoPerfil.html', {
        'aluno': aluno,
        'form': form
    })

#MONITOR_TUTOR========================================================================================

def monitor(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    monitor = get_object_or_404(Monitor, mon_cpf=user.username)
    return render(request, 'monitor_tutor/monitor.html', {
        'monitor': monitor
    })

def atualizarMonitorPerfil(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    monitor = get_object_or_404(Monitor, mon_cpf=user.username)

    form = AtualizarMonitoresForm(request.POST or None, instance=monitor)
    if form.is_valid():
        form.save()
        messages.success(request, 'Perfil alterado com sucesso!')
        return redirect('monitor', user.id)

    return render(request, 'monitor_tutor/atualizarMonitorPerfil.html', {
        'monitor': monitor,
        'form': form
    })

def tutor(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    tutor = get_object_or_404(Tutor, tut_cpf=user.username)
    return render(request, 'monitor_tutor/tutor.html', {
        'tutor' : tutor
    })

def atualizarTutorPerfil(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    tutor = get_object_or_404(Tutor, tut_cpf=user.username)

    form = AtualizarTutoresForm(request.POST or None, instance=tutor)
    if form.is_valid():
        form.save()
        messages.success(request, 'Perfil alterado com sucesso!')
        return redirect('tutor', user.id)

    return render(request, 'monitor_tutor/atualizarTutorPerfil.html', {
        'tutor': tutor,
        'form': form
    })

#INTERPRETE============================================================================================

def interprete(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    interprete = get_object_or_404(Interprete, int_cpf=user.username)
    return render(request, 'interpretes/interprete.html', {
        'interprete' : interprete
    })

def atualizarInterpretePerfil(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    interprete = get_object_or_404(Interprete, int_cpf=user.username)

    form = AtualizarInterpretesForm(request.POST or None, instance=interprete)
    if form.is_valid():
        form.save()
        messages.success(request, 'Perfil alterado com sucesso!')
        return redirect('interprete', user.id)

    return render(request, 'interpretes/atualizarInterpretePerfil.html', {
        'interprete': interprete,
        'form': form
    })

