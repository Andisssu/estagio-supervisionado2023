from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Acompanhamentos, AcompanhamentoMonitores, AcompanhamentoTutores, AcompanhamentoInterpretes, AcompanhamentoDisciplinas
from .forms import AcompanhamentosForm, AcoMonitoriasForm, AcoTutoriasForm, AcoInterpretacoesForm, AcoDisciplinasForm
from membros.models import CustomUser, Interprete, Monitor, Tutor, AlunoPcd

# def handle_uploaded_file(f):
#     with open('avisos/uploads/'+f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

#ADMIN=========================================================================================

def acoIndex(request):
    alunos = AlunoPcd.objects.all()
    acompanhamentos = Acompanhamentos.objects.order_by('-aco_id')
    paginator = Paginator(acompanhamentos, 10)

    page = request.GET.get('p')
    acompanhamentos = paginator.get_page(page)
    if not alunos:
        messages.warning(request,'Acompanhamentos não podem ser iniciados enquanto não existir alunos cadastrados nos sistema.')
    return render(request, 'acompanhamentos/acoIndex.html', {
        'acompanhamentos': acompanhamentos,
        'alunos': alunos
    })

def adicionarAcompanhamento(request):

    context = {}
    if request.POST:
        form = AcompanhamentosForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["avi_arquivos"])
            form.save()
            messages.success(request, "Acompanhamento iniciado com sucesso!")
            return redirect('acoIndex')
        else:
            form = AcompanhamentosForm(request.POST)
            messages.error(request, "As informações inseridas são inválidas! Tente novamente.")
    else:
        form = AcompanhamentosForm()
    context['form'] = form
    return render(request, 'acompanhamentos/adicionarAcompanhamento.html', context)

def acompanhamento(request, acompanhamento_id):
    acompanhamento = get_object_or_404(Acompanhamentos, aco_id=acompanhamento_id)
    try:
        monitoria = AcompanhamentoMonitores.objects.filter(AsMon_acompanhamento=acompanhamento).last()
    except:
        monitoria = None
    try:
        tutoria = AcompanhamentoTutores.objects.filter(AsTut_acompanhamento=acompanhamento).last()
    except:
        tutoria = None
    try:
        interpretacoes = AcompanhamentoInterpretes.objects.filter(AsInt_acompanhamento=acompanhamento)
    except:
        interpretacoes = None
    try:
        disciplinas = AcompanhamentoDisciplinas.objects.filter(AsDis_acompanhamento=acompanhamento)
    except:
        disciplinas = None

    return render(request, 'acompanhamentos/acompanhamento.html', {
        'acompanhamento': acompanhamento,
        'monitoria': monitoria,
        'tutoria': tutoria,
        'interpretacoes': interpretacoes,
        'disciplinas': disciplinas
    })

def atualizarAcompanhamento(request, acompanhamento_id):
    acompanhamento = get_object_or_404(Acompanhamentos, aco_id=acompanhamento_id)

    form = AcompanhamentosForm(request.POST or None, instance=acompanhamento)
    if form.is_valid():
        form.save()
        return redirect('acoIndex')

    return render(request, 'acompanhamentos/atualizarAcompanhamento.html', {
        'acompanhamento': acompanhamento,
        'form': form
    })

def buscarAcompanhamento(request):
    alunos = AlunoPcd.objects.all()
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            acompanhamentos = Acompanhamentos.objects.order_by('-aco_id').filter(
                Q(aco_semestre__icontains=searched) | Q(aco_aluno_pcd__alu_nome__icontains=searched)
            )
        else:
            acompanhamentos = None

        if not alunos:
            messages.warning(request,'Acompanhamentos não podem ser iniciados enquanto não existir alunos cadastrados nos sistema.')
        return render(request, 'acompanhamentos/buscarAcompanhamento.html', {
            'searched': searched,
            'acompanhamentos': acompanhamentos,
            'alunos': alunos
        })
    else:
        if not alunos:
            messages.warning(request,'Acompanhamentos não podem ser iniciados enquanto não existir alunos cadastrados nos sistema.')
        return render(request, 'acompanhamentos/buscarAcompanhamento.html', {
            'alunos': alunos
        })

def deletarAcompanhamento(request, acompanhamento_id):
    acompanhamento = get_object_or_404(Acompanhamentos, aco_id=acompanhamento_id)
    acompanhamento.delete()
    return redirect('acoIndex')

def acoDisIndex(request):
    disciplinas = AcompanhamentoDisciplinas.objects.order_by('-AsDis_id')
    paginator = Paginator(disciplinas, 10)

    page = request.GET.get('p')
    disciplinas = paginator.get_page(page)
    return render(request, 'acompanhamentos/acoDisIndex.html', {
        'disciplinas': disciplinas
    })

def adicionarDisciplina(request):

    context = {}
    if request.POST:
        form = AcoDisciplinasForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["avi_arquivos"])
            form.save()
            messages.success(request, "Disciplina vinculada com sucesso!")
            return redirect('acoDisIndex')
        else:
            form = AcoDisciplinasForm(request.POST)
            messages.error(request, "As informações inseridas são inválidas! Tente novamente.")
    else:
        form = AcoDisciplinasForm()
    context['form'] = form
    return render(request, 'acompanhamentos/adicionarDisciplina.html', context)

def atualizarDisciplina(request, disciplina_id):
    disciplina = get_object_or_404(AcompanhamentoDisciplinas, AsDis_id=disciplina_id)

    form = AcoDisciplinasForm(request.POST or None, instance=disciplina)
    if form.is_valid():
        form.save()
        return redirect('acoDisIndex')

    return render(request, 'acompanhamentos/atualizarDisciplina.html', {
        'disciplina': disciplina,
        'form': form
    })

def buscarDisciplina(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            disciplinas = AcompanhamentoDisciplinas.objects.order_by('-AsDis_id').filter(
                Q(AsDis_disciplina__dis_nome__icontains=searched) |
                Q(AsDis_acompanhamento__aco_aluno_pcd__alu_nome__icontains=searched ) |
                Q(AsDis_acompanhamento__aco_semestre__icontains=searched) |
                Q(AsDis_disciplina__dis_curso__cur_nome__icontains=searched)
            )
        else:
            disciplinas = None

        return render(request, 'acompanhamentos/buscarDisciplina.html', {
            'searched': searched,
            'disciplinas': disciplinas
        })
    else:
        return render(request, 'acompanhamentos/buscarDisciplina.html', {

        })

def deletarDisciplina(request, disciplina_id):
    disciplina = get_object_or_404(AcompanhamentoDisciplinas, AsDis_id=disciplina_id)
    disciplina.delete()
    return redirect('acoDisIndex')

def acoIntIndex(request):
    interpretes = Interprete.objects.all()
    interpretacoes = AcompanhamentoInterpretes.objects.order_by('-AsInt_id')
    paginator = Paginator(interpretacoes, 10)

    page = request.GET.get('p')
    interpretacoes = paginator.get_page(page)
    if not interpretes:
        messages.warning(request,'Interpretações não podem ser iniciadas enquanto não existir intérpretes cadastrados no sistema.')
    return render(request, 'acompanhamentos/acoIntIndex.html', {
        'interpretacoes': interpretacoes,
        'interpretes': interpretes
    })

def adicionarInterpretacao(request):

    context = {}
    if request.POST:
        form = AcoInterpretacoesForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["avi_arquivos"])
            form.save()
            messages.success(request, "Interpretação iniciada com sucesso!")
            return redirect('acoIntIndex')
        else:
            form = AcoInterpretacoesForm(request.POST)
            messages.error(request, "As informações inseridas são inválidas! Tente novamente.")
    else:
        form = AcoInterpretacoesForm()
    context['form'] = form
    return render(request, 'acompanhamentos/adicionarInterpretacao.html', context)

def atualizarInterpretacao(request, interpretacao_id):
    interpretacao = get_object_or_404(AcompanhamentoInterpretes, AsInt_id=interpretacao_id)

    form = AcoInterpretacoesForm(request.POST or None, instance=interpretacao)
    if form.is_valid():
        form.save()
        return redirect('acoIntIndex')

    return render(request, 'acompanhamentos/atualizarInterpretacao.html', {
        'interpretacao': interpretacao,
        'form': form
    })

def buscarInterpretacao(request):
    interpretes = Interprete.objects.all()
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            interpretacoes = AcompanhamentoInterpretes.objects.order_by('-AsInt_id').filter(
                Q(AsInt_interprete__int_nome__icontains=searched) |
                Q(AsInt_acompanhamento__aco_aluno_pcd__alu_nome__icontains=searched) |
                Q(AsInt_acompanhamento__aco_semestre__icontains=searched)
            )
        else:
            interpretacoes = None

        if not interpretes:
            messages.warning(request,'Interpretações não podem ser iniciadas enquanto não existir intérpretes cadastrados no sistema.')
        return render(request, 'acompanhamentos/buscarInterpretacao.html', {
            'searched': searched,
            'interpretacoes': interpretacoes,
            'interpretes': interpretes
        })
    else:
        if not interpretes:
            messages.warning(request,'Interpretações não podem ser iniciadas enquanto não existir intérpretes cadastrados no sistema.')
        return render(request, 'acompanhamentos/buscarInterpretacao.html', {
            'interpretes': interpretes
        })

def deletarInterpretacao(request, interpretacao_id):
    interpretacao = get_object_or_404(AcompanhamentoInterpretes, AsInt_id=interpretacao_id)
    interpretacao.delete()
    return redirect('acoIntIndex')

def acoMonIndex(request):
    monitores = Monitor.objects.all()
    monitorias = AcompanhamentoMonitores.objects.order_by('-AsMon_id')
    paginator = Paginator(monitorias, 10)

    page = request.GET.get('p')
    monitorias = paginator.get_page(page)
    if not monitores:
        messages.warning(request, 'Monitorias não podem ser iniciadas enquanto não existir monitores cadastrados no sistema.')
    return render(request, 'acompanhamentos/acoMonIndex.html', {
        'monitorias': monitorias,
        'monitores': monitores
    })

def adicionarMonitoria(request):

    context = {}
    if request.POST:
        form = AcoMonitoriasForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["avi_arquivos"])
            form.save()
            messages.success(request, "Monitoria iniciada com sucesso!")
            return redirect('acoMonIndex')
        else:
            form = AcoMonitoriasForm(request.POST)
            messages.error(request, "As informações inseridas são inválidas! Tente novamente.")
    else:
        form = AcoMonitoriasForm()
    context['form'] = form
    return render(request, 'acompanhamentos/adicionarMonitoria.html', context)

def atualizarMonitoria(request, monitoria_id):
    monitoria = get_object_or_404(AcompanhamentoMonitores, AsMon_id=monitoria_id)

    form = AcoMonitoriasForm(request.POST or None, instance=monitoria)
    if form.is_valid():
        form.save()
        return redirect('acoMonIndex')

    return render(request, 'acompanhamentos/atualizarMonitoria.html', {
        'monitoria': monitoria,
        'form': form
    })

def buscarMonitoria(request):
    monitores = Monitor.objects.all()
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            monitorias = AcompanhamentoMonitores.objects.order_by('-AsMon_id').filter(
                Q(AsMon_monitor__mon_nome__icontains=searched) |
                Q(AsMon_acompanhamento__aco_aluno_pcd__alu_nome__icontains=searched) |
                Q(AsMon_acompanhamento__aco_semestre__icontains=searched)
            )
        else:
            monitorias = None

        if not monitores:
            messages.warning(request, 'Monitorias não podem ser iniciadas enquanto não existir monitores cadastrados no sistema.')
        return render(request, 'acompanhamentos/buscarMonitoria.html', {
            'searched': searched,
            'monitorias': monitorias,
            'monitores': monitores
        })
    else:
        if not monitores:
            messages.warning(request, 'Monitorias não podem ser iniciadas enquanto não existir monitores cadastrados no sistema.')
        return render(request, 'acompanhamentos/buscarMonitoria.html', {
            'monitores': monitores
        })

def deletarMonitoria(request, monitoria_id):
    monitoria = get_object_or_404(AcompanhamentoMonitores, AsMon_id=monitoria_id)
    monitoria.delete()
    return redirect('acoMonIndex')

def acoTutIndex(request):
    tutores = Tutor.objects.all()
    tutorias = AcompanhamentoTutores.objects.order_by('-AsTut_id')
    paginator = Paginator(tutorias, 10)

    page = request.GET.get('p')
    tutorias = paginator.get_page(page)
    if not tutores:
        messages.warning(request, 'Tutorias não podem ser iniciadas enquanto não existir tutores cadastrados no sistema.')
    return render(request, 'acompanhamentos/acoTutIndex.html', {
        'tutorias': tutorias,
        'tutores': tutores
    })

def adicionarTutoria(request):

    context = {}
    if request.POST:
        form = AcoTutoriasForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["avi_arquivos"])
            form.save()
            messages.success(request, "Tutoria iniciada com sucesso!")
            return redirect('acoTutIndex')
        else:
            form = AcoTutoriasForm(request.POST)
            messages.error(request, "As informações inseridas são inválidas! Tente novamente.")
    else:
        form = AcoTutoriasForm()
    context['form'] = form
    return render(request, 'acompanhamentos/adicionarTutoria.html', context)

def atualizarTutoria(request, tutoria_id):
    tutoria = get_object_or_404(Acompanhamentos, AsTut_id=tutoria_id)

    form = AcoTutoriasForm(request.POST or None, instance=tutoria)
    if form.is_valid():
        form.save()
        return redirect('acoTutIndex')

    return render(request, 'acompanhamentos/atualizarTutoria.html', {
        'tutoria': tutoria,
        'form': form
    })

def buscarTutoria(request):
    tutores = Tutor.objects.all()
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            tutorias = AcompanhamentoTutores.objects.order_by('-AsTut_id').filter(
                Q(AsTut_tutor__tut_nome__icontains=searched) |
                Q(AsTut_acompanhamento__aco_aluno_pcd__alu_nome__icontains=searched) |
                Q(AsTut_acompanhamento__aco_semestre__icontains=searched)
            )
        else:
            tutorias = None

        if not tutores:
            messages.warning(request, 'Tutorias não podem ser iniciadas enquanto não existir tutores cadastrados no sistema.')
        return render(request, 'acompanhamentos/buscarTutoria.html', {
            'searched': searched,
            'tutorias': tutorias,
            'tutores': tutores
        })
    else:
        if not tutores:
            messages.warning(request, 'Tutorias não podem ser iniciadas enquanto não existir tutores cadastrados no sistema.')
        return render(request, 'acompanhamentos/buscarTutoria.html', {
            'tutores': tutores
        })

def deletarTutoria(request, tutoria_id):
    tutoria = get_object_or_404(AcompanhamentoTutores, AsTut_id=tutoria_id)
    tutoria.delete()
    return redirect('acoTutIndex')

#ALUNOS========================================================================================
def acoDisIndexAluno(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    aluno = get_object_or_404(AlunoPcd, alu_cpf=user.username)
    acompanhamento = Acompanhamentos.objects.filter(aco_aluno_pcd=aluno).last()
    disciplinas = AcompanhamentoDisciplinas.objects.order_by('-AsDis_id').filter(
        AsDis_acompanhamento=acompanhamento
    )
    paginator = Paginator(disciplinas, 10)

    page = request.GET.get('p')
    disciplinas = paginator.get_page(page)
    return render(request, 'acompanhamentos/acoDisIndexAluno.html', {
        'disciplinas': disciplinas
    })

def acompanhamentoAluno(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    aluno = get_object_or_404(AlunoPcd, alu_cpf=user.username)
    acompanhamento = Acompanhamentos.objects.filter(aco_aluno_pcd=aluno).last()
    try:
        monitoria = AcompanhamentoMonitores.objects.filter(AsMon_acompanhamento=acompanhamento).last()
    except:
        monitoria = None
    try:
        tutoria = AcompanhamentoTutores.objects.filter(AsTut_acompanhamento=acompanhamento).last()
    except:
        tutoria = None
    try:
        interpretacoes = AcompanhamentoInterpretes.objects.filter(AsInt_acompanhamento=acompanhamento)
    except:
        interpretacoes = None

    return render(request, 'acompanhamentos/acompanhamentoAluno.html', {
        'acompanhamento': acompanhamento,
        'monitoria': monitoria,
        'tutoria': tutoria,
        'interpretacoes': interpretacoes,
    })

def buscarDisciplinaAluno(request, user_id):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            user = get_object_or_404(CustomUser, id=user_id)
            aluno = get_object_or_404(AlunoPcd, alu_cpf=user.username)
            acompanhamento = Acompanhamentos.objects.filter(aco_aluno_pcd=aluno).last()
            disciplinas = AcompanhamentoDisciplinas.objects.order_by('-AsDis_id').filter(
                Q(AsDis_disciplina__dis_nome__icontains=searched) |
                Q(AsDis_disciplina__dis_curso__cur_nome__icontains=searched)
            ).filter(
                AsDis_acompanhamento=acompanhamento
            )
        else:
            disciplinas = None

        return render(request, 'acompanhamentos/buscarDisciplinaAluno.html', {
            'searched': searched,
            'disciplinas': disciplinas
        })
    else:
        return render(request, 'acompanhamentos/buscarDisciplinaAluno.html', {

        })

#MONITORES=====================================================================================
def acoIndexMonitor(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    monitor = get_object_or_404(Monitor, mon_cpf=user.username)
    monitorias = AcompanhamentoMonitores.objects.filter(AsMon_monitor=monitor)
    acompanhamentos = Acompanhamentos.objects.filter(
        aco_id__in=[m.AsMon_acompanhamento.aco_id for m in monitorias.all()]
    )
    paginator = Paginator(acompanhamentos, 10)

    page = request.GET.get('p')
    acompanhamentos = paginator.get_page(page)
    return render(request, 'acompanhamentos/acoIndexMonitor.html', {
        'acompanhamentos': acompanhamentos
    })

def acoDisIndexMonitor(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    monitor = get_object_or_404(Monitor, mon_cpf=user.username)
    monitorias = AcompanhamentoMonitores.objects.filter(AsMon_monitor=monitor)
    acompanhamentos = Acompanhamentos.objects.filter(
        aco_id__in=[m.AsMon_acompanhamento.aco_id for m in monitorias.all()]
    )
    disciplinas = AcompanhamentoDisciplinas.objects.order_by('-AsDis_id').filter(
        AsDis_acompanhamento__in=[a for a in acompanhamentos.all()]
    )
    paginator = Paginator(disciplinas, 10)

    page = request.GET.get('p')
    disciplinas = paginator.get_page(page)
    return render(request, 'acompanhamentos/acoDisIndexMonitor.html', {
        'disciplinas': disciplinas
    })

def acompanhamentoMonitor(request, acompanhamento_id):
    acompanhamento = get_object_or_404(Acompanhamentos, aco_id=acompanhamento_id)
    try:
        monitoria = AcompanhamentoMonitores.objects.filter(AsMon_acompanhamento=acompanhamento).last()
    except:
        monitoria = None
    try:
        tutoria = AcompanhamentoTutores.objects.filter(AsTut_acompanhamento=acompanhamento).last()
    except:
        tutoria = None
    try:
        interpretacoes = AcompanhamentoInterpretes.objects.filter(AsInt_acompanhamento=acompanhamento)
    except:
        interpretacoes = None
    try:
        disciplinas = AcompanhamentoDisciplinas.objects.filter(AsDis_acompanhamento=acompanhamento)
    except:
        disciplinas = None

    return render(request, 'acompanhamentos/acompanhamentoMonitor.html', {
        'acompanhamento': acompanhamento,
        'monitoria': monitoria,
        'tutoria': tutoria,
        'interpretacoes': interpretacoes,
        'disciplinas': disciplinas
    })

def buscarAcompanhamentoMonitor(request, user_id):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            user = get_object_or_404(CustomUser, id=user_id)
            monitor = get_object_or_404(Monitor, mon_cpf=user.username)
            monitorias = AcompanhamentoMonitores.objects.filter(AsMon_monitor=monitor)
            acompanhamentos = Acompanhamentos.objects.order_by('-aco_id').filter(
                Q(aco_semestre__icontains=searched) | Q(aco_aluno_pcd__alu_nome__icontains=searched)
            ).filter(
                aco_id__in=[m.AsMon_acompanhamento.aco_id for m in monitorias.all()]
            )
        else:
            acompanhamentos = None

        return render(request, 'acompanhamentos/buscarAcompanhamentoMonitor.html', {
            'searched': searched,
            'acompanhamentos': acompanhamentos
        })
    else:
        return render(request, 'acompanhamentos/buscarAcompanhamentoMonitor.html', {

        })

def buscarDisciplinaMonitor(request, user_id):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            user = get_object_or_404(CustomUser, id=user_id)
            monitor = get_object_or_404(Monitor, mon_cpf=user.username)
            monitorias = AcompanhamentoMonitores.objects.filter(AsMon_monitor=monitor)
            acompanhamentos = Acompanhamentos.objects.filter(
                aco_id__in=[m.AsMon_acompanhamento.aco_id for m in monitorias.all()]
            )
            disciplinas = AcompanhamentoDisciplinas.objects.order_by('-AsDis_id').filter(
                Q(AsDis_disciplina__dis_nome__icontains=searched) |
                Q(AsDis_acompanhamento__aco_aluno_pcd__alu_nome__icontains=searched) |
                Q(AsDis_acompanhamento__aco_semestre__icontains=searched) |
                Q(AsDis_disciplina__dis_curso__cur_nome__icontains=searched)
            ).filter(
                AsDis_acompanhamento__in=[a for a in acompanhamentos.all()]
            )
        else:
            disciplinas = None

        return render(request, 'acompanhamentos/buscarDisciplinaMonitor.html', {
            'searched': searched,
            'disciplinas': disciplinas
        })
    else:
        return render(request, 'acompanhamentos/buscarDisciplinaMonitor.html', {

        })

#TUTORES=======================================================================================
def acoIndexTutor(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    tutor = get_object_or_404(Tutor, tut_cpf=user.username)
    tutorias = AcompanhamentoTutores.objects.filter(AsTut_tutor=tutor)
    acompanhamentos = Acompanhamentos.objects.order_by('-aco_id').filter(
        aco_id__in=[t.AsTut_acompanhamento.aco_id for t in tutorias.all()]
    )
    paginator = Paginator(acompanhamentos, 10)

    page = request.GET.get('p')
    acompanhamentos = paginator.get_page(page)
    return render(request, 'acompanhamentos/acoIndexTutor.html', {
        'acompanhamentos': acompanhamentos
    })

def acoDisIndexTutor(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    tutor = get_object_or_404(Tutor, tut_cpf=user.username)
    tutorias = AcompanhamentoTutores.objects.filter(AsTut_tutor=tutor)
    acompanhamentos = Acompanhamentos.objects.filter(
        aco_id__in=[t.AsTut_acompanhamento.aco_id for t in tutorias.all()]
    )
    disciplinas = AcompanhamentoDisciplinas.objects.order_by('-AsDis_id').filter(
        AsDis_acompanhamento__in=[a for a in acompanhamentos.all()]
    )
    paginator = Paginator(disciplinas, 10)

    page = request.GET.get('p')
    disciplinas = paginator.get_page(page)
    return render(request, 'acompanhamentos/acoDisIndexTutor.html', {
        'disciplinas': disciplinas
    })

def acompanhamentoTutor(request, acompanhamento_id):
    acompanhamento = get_object_or_404(Acompanhamentos, aco_id=acompanhamento_id)
    try:
        monitoria = AcompanhamentoMonitores.objects.filter(AsMon_acompanhamento=acompanhamento).last()
    except:
        monitoria = None
    try:
        tutoria = AcompanhamentoTutores.objects.filter(AsTut_acompanhamento=acompanhamento).last()
    except:
        tutoria = None
    try:
        interpretacoes = AcompanhamentoInterpretes.objects.filter(AsInt_acompanhamento=acompanhamento)
    except:
        interpretacoes = None
    try:
        disciplinas = AcompanhamentoDisciplinas.objects.filter(AsDis_acompanhamento=acompanhamento)
    except:
        disciplinas = None

    return render(request, 'acompanhamentos/acompanhamentoTutor.html', {
        'acompanhamento': acompanhamento,
        'monitoria': monitoria,
        'tutoria': tutoria,
        'interpretacoes': interpretacoes,
        'disciplinas': disciplinas
    })

def buscarAcompanhamentoTutor(request, user_id):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            user = get_object_or_404(CustomUser, id=user_id)
            tutor = get_object_or_404(Tutor, tut_cpf=user.username)
            tutorias = AcompanhamentoTutores.objects.filter(AsTut_tutor=tutor)
            acompanhamentos = Acompanhamentos.objects.order_by('-aco_id').filter(
                Q(aco_semestre__icontains=searched) | Q(aco_aluno_pcd__alu_nome__icontains=searched)
            ).filter(
                aco_id__in=[t.AsTut_acompanhamento.aco_id for t in tutorias.all()]
            )
        else:
            acompanhamentos = None

        return render(request, 'acompanhamentos/buscarAcompanhamentoTutor.html', {
            'searched': searched,
            'acompanhamentos': acompanhamentos
        })
    else:
        return render(request, 'acompanhamentos/buscarAcompanhamentoTutor.html', {

        })

def buscarDisciplinaTutor(request, user_id):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            user = get_object_or_404(CustomUser, id=user_id)
            tutor = get_object_or_404(Tutor, tut_cpf=user.username)
            tutorias = AcompanhamentoTutores.objects.filter(AsTut_tutor=tutor)
            acompanhamentos = Acompanhamentos.objects.filter(
                aco_id__in=[t.AsTut_acompanhamento.aco_id for t in tutorias.all()]
            )
            disciplinas = AcompanhamentoDisciplinas.objects.order_by('-AsDis_id').filter(
                Q(AsDis_disciplina__dis_nome__icontains=searched) |
                Q(AsDis_acompanhamento__aco_aluno_pcd__alu_nome__icontains=searched) |
                Q(AsDis_acompanhamento__aco_semestre__icontains=searched) |
                Q(AsDis_disciplina__dis_curso__cur_nome__icontains=searched)
            ).filter(
                AsDis_acompanhamento__in=[a for a in acompanhamentos.all()]
            )
        else:
            disciplinas = None

        return render(request, 'acompanhamentos/buscarDisciplinaTutor.html', {
            'searched': searched,
            'disciplinas': disciplinas
        })
    else:
        return render(request, 'acompanhamentos/buscarDisciplinaTutor.html', {

        })

#INTERPRETES===================================================================================
def acoIndexInterprete(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    interprete = get_object_or_404(Interprete, int_cpf=user.username)
    interpretacoes = AcompanhamentoInterpretes.objects.filter(AsInt_interprete=interprete)
    acompanhamentos = Acompanhamentos.objects.order_by('-aco_id').filter(
            aco_id__in=[i.AsInt_acompanhamento.aco_id for i in interpretacoes.all()]
        )
    paginator = Paginator(acompanhamentos, 10)

    page = request.GET.get('p')
    acompanhamentos = paginator.get_page(page)
    return render(request, 'acompanhamentos/acoIndexInterprete.html', {
        'acompanhamentos': acompanhamentos
    })

def acoDisIndexInterprete(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    interprete = get_object_or_404(Interprete, int_cpf=user.username)
    interpretacoes = AcompanhamentoInterpretes.objects.filter(AsInt_interprete=interprete)
    acompanhamentos = Acompanhamentos.objects.filter(
        aco_id__in=[i.AsInt_acompanhamento.aco_id for i in interpretacoes.all()]
    )
    disciplinas = AcompanhamentoDisciplinas.objects.order_by('-AsDis_id').filter(
        AsDis_acompanhamento__in=[a for a in acompanhamentos.all()]
    )
    paginator = Paginator(disciplinas, 10)

    page = request.GET.get('p')
    disciplinas = paginator.get_page(page)
    return render(request, 'acompanhamentos/acoDisIndexInterprete.html', {
        'disciplinas': disciplinas
    })

def acompanhamentoInterprete(request, acompanhamento_id):
    acompanhamento = get_object_or_404(Acompanhamentos, aco_id=acompanhamento_id)
    try:
        monitoria = AcompanhamentoMonitores.objects.filter(AsMon_acompanhamento=acompanhamento).last()
    except:
        monitoria = None
    try:
        tutoria = AcompanhamentoTutores.objects.filter(AsTut_acompanhamento=acompanhamento).last()
    except:
        tutoria = None
    try:
        interpretacoes = AcompanhamentoInterpretes.objects.filter(AsInt_acompanhamento=acompanhamento)
    except:
        interpretacoes = None
    try:
        disciplinas = AcompanhamentoDisciplinas.objects.filter(AsDis_acompanhamento=acompanhamento)
    except:
        disciplinas = None

    return render(request, 'acompanhamentos/acompanhamentoInterprete.html', {
        'acompanhamento': acompanhamento,
        'monitoria': monitoria,
        'tutoria': tutoria,
        'interpretacoes': interpretacoes,
        'disciplinas': disciplinas
    })

def buscarAcompanhamentoInterprete(request, user_id):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            user = get_object_or_404(CustomUser, id=user_id)
            interprete = get_object_or_404(Interprete, int_cpf=user.username)
            interpretacoes = AcompanhamentoInterpretes.objects.filter(AsInt_interprete=interprete)
            acompanhamentos = Acompanhamentos.objects.order_by('-aco_id').filter(
                Q(aco_semestre__icontains=searched) | Q(aco_aluno_pcd__alu_nome__icontains=searched)
            ).filter(
                aco_id__in=[i.AsInt_acompanhamento.aco_id for i in interpretacoes.all()]
            )
        else:
            acompanhamentos = None

        return render(request, 'acompanhamentos/buscarAcompanhamentoInterprete.html', {
            'searched': searched,
            'acompanhamentos': acompanhamentos
        })
    else:
        return render(request, 'acompanhamentos/buscarAcompanhamentoInterprete.html', {

        })

def buscarDisciplinaInterprete(request, user_id):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            user = get_object_or_404(CustomUser, id=user_id)
            interprete = get_object_or_404(Interprete, int_cpf=user.username)
            interpretacoes = AcompanhamentoInterpretes.objects.filter(AsInt_interprete=interprete)
            acompanhamentos = Acompanhamentos.objects.filter(
                aco_id__in=[i.AsInt_acompanhamento.aco_id for i in interpretacoes.all()]
            )
            disciplinas = AcompanhamentoDisciplinas.objects.order_by('-AsDis_id').filter(
                Q(AsDis_disciplina__dis_nome__icontains=searched) |
                Q(AsDis_acompanhamento__aco_aluno_pcd__alu_nome__icontains=searched ) |
                Q(AsDis_acompanhamento__aco_semestre__icontains=searched) |
                Q(AsDis_disciplina__dis_curso__cur_nome__icontains=searched)
            ).filter(
                AsDis_acompanhamento__in=[a for a in acompanhamentos.all()]
            )
        else:
            disciplinas = None

        return render(request, 'acompanhamentos/buscarDisciplinaInterprete.html', {
            'searched': searched,
            'disciplinas': disciplinas
        })
    else:
        return render(request, 'acompanhamentos/buscarDisciplinaInterprete.html', {

        })