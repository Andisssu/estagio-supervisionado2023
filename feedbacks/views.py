import os
import mimetypes
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Feedbacks
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import FeedbacksForm, FeedbacksRespostaForm, FeedbacksMonitorForm, FeedbacksTutorForm

from membros.models import AlunoPcd, CustomUser, Monitor, Tutor
from acompanhamentos.models import Acompanhamentos, AcompanhamentoMonitores, AcompanhamentoTutores

# def handle_uploaded_file(f):
#     with open('avisos/uploads/'+f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
def feeIndex(request):
    feedbacks = Feedbacks.objects.filter(fee_anterior=None)


    paginator = Paginator(feedbacks, 5)

    page = request.GET.get('p')
    feedbacks = paginator.get_page(page)

    feedbacks = reversed(feedbacks)
    return render(request, 'feedbacks/feeIndex.html', {
        'feedbacks': feedbacks
    })

def adicionarFeedback(request):
    submitted = False

    context = {}
    if request.POST:
        form = FeedbacksForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["avi_arquivos"])
            form.save()
            return HttpResponseRedirect('adicionarFeedback?submitted=True')
        else:
            form = FeedbacksForm()
            form.save()
            return HttpResponseRedirect('adicionarFeedback?submitted=True')
    else:
        form = FeedbacksForm()
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted
    return render(request, 'feedbacks/adicionarFeedback.html', context)

def feedback(request, feedback_id):
    feedback = get_object_or_404(Feedbacks, fee_id=feedback_id)

    return render(request, 'feedbacks/feedback.html', {
        'feedback': feedback
    })

def atualizarFeedback(request, feedback_id):
    feedback = get_object_or_404(Feedbacks, fee_id=feedback_id)

    form = FeedbacksForm(request.POST or None, instance=feedback)
    if form.is_valid():
        form.save()
        return redirect('feeIndex')

    return render(request, 'feedbacks/atualizarFeedback.html', {
        'feedback': feedback,
        'form': form
    })

def buscarFeedback(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            feedbacks = Feedbacks.objects.order_by('-fee_id').filter(Q(fee_titulo__icontains=searched) | Q(fee_descricao__icontains=searched) )
        else:
            feedbacks = None

        return render(request, 'feedbacks/buscarFeedback.html', {
            'searched': searched,
            'feedbacks': feedbacks
        })
    else:
        return render(request, 'feedbacks/buscarFeedback.html', {

        })

def baixarFileFeedback(request, filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = str(filename)
    filepath = BASE_DIR + '\\uploads\\' + filename
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

#ADMIN-FEEDBACK
def adminFeedbackAll(request):
    feedback = Feedbacks.objects.order_by('-fee_id').filter(fee_anterior=None)

    paginator = Paginator(feedback, 7)
    page = request.GET.get('p')
    feedback = paginator.get_page(page)

    return render(request, 'feedbacks/adminFeedbackAll.html', {
        'feedback': feedback,
    })

def adminOpenAllfeedback(request, feedback_id):
    feedbackInicial = get_object_or_404(Feedbacks, fee_id=feedback_id)
    list_feedback = Feedbacks.objects.all()

    feedback = []
    f0 = feedbackInicial
    feedback.append(f0)
    ultimo_feedback = None
    for f1 in list_feedback:
        if f1.fee_anterior == f0.fee_id:
            feedback.append(f1)
            f0=f1
            if f1.fee_proximo == None:
                ultimo_feedback = f1
                break
    feedback = reversed(feedback)
    return render(request, 'feedbacks/adminOpenAllfeedback.html', {
        'feedback': feedback,
        'ultimo_feedback': ultimo_feedback,
        'feedbackInicial': feedbackInicial
    })
def adminOpenfeedback(request, feedback_id):
    feedback = get_object_or_404(Feedbacks, fee_id=feedback_id)

    if feedback.fee_proximo != None:
        return adminOpenAllfeedback(request, feedback_id)
    return render(request, 'feedbacks/adminOpenfeedback.html', {
        'feedback': feedback

    })

def adminRespostaFeedback(request, feedback_id):
    submitted = False
    context = {}

    if request.POST:
        form = FeedbacksRespostaForm(request.POST, request.FILES)

        if form.is_valid():
            Feedbackform = form.save(commit=False)
            ultimo_feedback = get_object_or_404(Feedbacks, fee_id=feedback_id)

            Feedbackform.fee_titulo = ultimo_feedback.fee_titulo
            Feedbackform.fee_emissor = request.user
            Feedbackform.fee_anterior = ultimo_feedback.fee_id
            Feedbackform.fee_acompanhamento = ultimo_feedback.fee_acompanhamento
            if ultimo_feedback.fee_inicial:
                Feedbackform.fee_inicial = ultimo_feedback.fee_inicial
            else:
                Feedbackform.fee_inicial = ultimo_feedback.fee_id
            Feedbackform.fee_new = True

            Feedbackform.save()
            print(Feedbackform.fee_id)
            ultimo_feedback.fee_proximo = Feedbackform.fee_id
            ultimo_feedback.save()
            messages.success(request, "Feedback de resposta enviado com sucesso!")
            return redirect('adminFeedbackAll')

        else:
            form = FeedbacksRespostaForm()
            return HttpResponseRedirect('adminRespostaFeedback?submitted=True')
    else:
        form = FeedbacksRespostaForm()
        if 'submitted' in request.GET:
            submitted = True

    context['form'] = form
    context['submitted'] = submitted

    return render(request, 'feedbacks/adminRespostaFeedback.html', context)

def adminDeletarFeedback(request, feedback_id):
    feedbackInicial = get_object_or_404(Feedbacks, fee_id=feedback_id)
    list_feedback = Feedbacks.objects.all()

    feedbacks = []
    f0 = feedbackInicial
    feedbacks.append(f0)
    for f1 in list_feedback:
        if f1.fee_anterior == f0.fee_id:
            feedbacks.append(f1)
            f0 = f1
            if f1.fee_proximo == None:
                break
    while feedbacks:
        f = feedbacks.pop()
        arquivo_nome = f.fee_arquivo
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = BASE_DIR + '\\uploads\\' + str(arquivo_nome)
        f.delete()
        try:
            os.remove(filepath)
        except:
            pass
    return redirect('adminFeedbackAll')

def adminMarcarComoLido(request, feedback_id):
    feedback = Feedbacks.objects.filter(fee_id=feedback_id)
    feedback.fee_new = False
    feedback.save()
    messages.success(request, "Feedback marcado como lido!.")
    return redirect('adminFeedbackAll')

#ALUNO-FEEDBACK
def alunoFeedback(request, user_id):
    submitted = False
    context = {}

    if request.POST:
        form = FeedbacksForm(request.POST, request.FILES)
        user = get_object_or_404(CustomUser, id=user_id)
        aluno = get_object_or_404(AlunoPcd, alu_cpf=user.username)
        acompanhamento = Acompanhamentos.objects.filter(aco_aluno_pcd = aluno).last()

        if form.is_valid():
            Feedbackform = form.save(commit=False)
            Feedbackform.fee_acompanhamento = acompanhamento
            Feedbackform.fee_emissor = user
            Feedbackform.fee_new = True
            Feedbackform.save()
            messages.success(request, "Feedback iniciado com sucesso!")
            return redirect('alunoFeedbackAll', user_id)
        else:
            form = FeedbacksForm()
    else:
        form = FeedbacksForm()
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted

    return render (request, 'feedbacks/alunoFeedback.html', context)

def alunoFeedbackAll(request, user_id):

    user = get_object_or_404(CustomUser, id=user_id)
    aluno = get_object_or_404(AlunoPcd, alu_cpf=user.username)
    acompanhamentos = Acompanhamentos.objects.filter(aco_aluno_pcd = aluno)
    feedback = Feedbacks.objects.order_by('-fee_id').filter(fee_acompanhamento__in=[a.aco_id for a in acompanhamentos.all()], fee_anterior=None )

    paginator = Paginator(feedback, 7)
    page = request.GET.get('p')
    feedback = paginator.get_page(page)

    return render(request, 'feedbacks/alunoFeedbackAll.html', {
        'feedback': feedback,
        'acompanhamentos': acompanhamentos,
    })

def alunoOpenAllfeedback(request, user_id, feedback_id):

    user = get_object_or_404(CustomUser, id=user_id)
    aluno = get_object_or_404(AlunoPcd, alu_cpf=user.username)
    feedbackInicial = get_object_or_404(Feedbacks, fee_id=feedback_id)
    acompanhamentos = Acompanhamentos.objects.filter(aco_aluno_pcd = aluno.alu_id)
    list_feedback = Feedbacks.objects.filter(fee_acompanhamento__in=[a.aco_id for a in acompanhamentos.all()])

    feedback = []
    f0 = feedbackInicial
    feedback.append(f0)
    ultimo_feedback = None
    for f1 in list_feedback:
        if f1.fee_anterior == f0.fee_id:
            feedback.append(f1)
            f0=f1
            if f1.fee_proximo == None:
                ultimo_feedback = f1
                break
    feedback = reversed(feedback)
    return render(request, 'feedbacks/alunoOpenAllfeedback.html', {
        'feedback': feedback,
        'ultimo_feedback': ultimo_feedback,
        'feedbackInicial': feedbackInicial
    })
def alunoOpenfeedback(request, user_id, feedback_id ):
    feedback = get_object_or_404(Feedbacks, fee_id=feedback_id)

    if feedback.fee_proximo != None:
        return alunoOpenAllfeedback(request, user_id, feedback_id)
    return render(request, 'feedbacks/alunoOpenfeedback.html', {
        'feedback': feedback

    })

def alunoRespostaFeedback(request, user_id, feedback_id):
    submitted = False
    context = {}

    if request.POST:
        form = FeedbacksRespostaForm(request.POST, request.FILES)

        if form.is_valid():
            Feedbackform = form.save(commit=False)
            ultimo_feedback = get_object_or_404(Feedbacks, fee_id=feedback_id)

            Feedbackform.fee_titulo = ultimo_feedback.fee_titulo
            Feedbackform.fee_emissor = request.user
            Feedbackform.fee_anterior = ultimo_feedback.fee_id
            Feedbackform.fee_acompanhamento = ultimo_feedback.fee_acompanhamento
            if ultimo_feedback.fee_inicial:
                Feedbackform.fee_inicial = ultimo_feedback.fee_inicial
            else:
                Feedbackform.fee_inicial = ultimo_feedback.fee_id
            Feedbackform.fee_new = True

            Feedbackform.save()
            print(Feedbackform.fee_id)
            ultimo_feedback.fee_proximo = Feedbackform.fee_id
            ultimo_feedback.save()
            messages.success(request, "Feedback de resposta enviado com sucesso!")
            return redirect('alunoFeedbackAll', user_id)

        else:
            form = FeedbacksRespostaForm()
            return HttpResponseRedirect('alunoRespostaFeedback?submitted=True')
    else:
        form = FeedbacksRespostaForm()
        if 'submitted' in request.GET:
            submitted = True

    context['form'] = form
    context['submitted'] = submitted

    return render(request, 'feedbacks/alunoRespostaFeedback.html', context)

def alunoMarcarComoLido(request, feedback_id):
    feedback = Feedbacks.objects.filter(fee_id=feedback_id)
    feedback.fee_new = False
    feedback.save()
    user = get_object_or_404(CustomUser, id=request.user.id)
    messages.success(request, "Feedback marcado como lido!.")
    return redirect('alunoFeedbackAll', user.id)

#MONITOR-FEEDBACK
def monitorFeedback(request, user_id):
    submitted = False
    context = {}

    user = get_object_or_404(CustomUser, id=user_id)
    if request.POST:
        form = FeedbacksMonitorForm(user, request.POST, request.FILES)

        if form.is_valid():
            Feedbackform = form.save(commit=False)
            Feedbackform.fee_emissor = user
            Feedbackform.fee_new = True
            Feedbackform.save()
            messages.success(request, "Feedback iniciado com sucesso!")
            return redirect('monitorFeedbackAll', user_id)
        else:
            form = FeedbacksMonitorForm(user)
            return HttpResponseRedirect('monitorFeedback?submitted=True')
    else:
        form = FeedbacksMonitorForm(user)
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted

    return render (request, 'feedbacks/monitorFeedback.html', context)

def monitorFeedbackAll(request, user_id):

    user = get_object_or_404(CustomUser, id=user_id)
    monitor = get_object_or_404(Monitor, mon_cpf=user.username)
    monitorias = AcompanhamentoMonitores.objects.filter(AsMon_monitor=monitor)
    acompanhamentos = Acompanhamentos.objects.filter(aco_id__in=[m.AsMon_acompanhamento.aco_id for m in monitorias.all()])
    feedback = Feedbacks.objects.order_by('-fee_id').filter(fee_acompanhamento__in=[a.aco_id for a in acompanhamentos.all()], fee_anterior=None )

    paginator = Paginator(feedback, 7)
    page = request.GET.get('p')
    feedback = paginator.get_page(page)

    return render(request, 'feedbacks/monitorFeedbackAll.html', {
        'feedback': feedback,
        'acompanhamentos': acompanhamentos,
    })

def monitorOpenAllfeedback(request, user_id, feedback_id):

    user = get_object_or_404(CustomUser, id=user_id)
    monitor = get_object_or_404(Monitor, mon_cpf=user.username)
    monitorias = AcompanhamentoMonitores.objects.filter(AsMon_monitor=monitor)
    feedbackInicial = get_object_or_404(Feedbacks, fee_id=feedback_id)
    acompanhamentos = Acompanhamentos.objects.filter(aco_id__in=[m.AsMon_acompanhamento.aco_id for m in monitorias.all()])
    list_feedback = Feedbacks.objects.filter(fee_acompanhamento__in=[a.aco_id for a in acompanhamentos.all()])

    feedback = []
    f0 = feedbackInicial
    feedback.append(f0)
    ultimo_feedback = None
    for f1 in list_feedback:
        if f1.fee_anterior == f0.fee_id:
            feedback.append(f1)
            f0=f1
            if f1.fee_proximo == None:
                ultimo_feedback = f1
                break
    feedback = reversed(feedback)
    return render(request, 'feedbacks/monitorOpenAllfeedback.html', {
        'feedback': feedback,
        'ultimo_feedback': ultimo_feedback,
        'feedbackInicial': feedbackInicial
    })
def monitorOpenfeedback(request, user_id, feedback_id):
    feedback = get_object_or_404(Feedbacks, fee_id=feedback_id)

    if feedback.fee_proximo != None:
        return monitorOpenAllfeedback(request, user_id, feedback_id)
    return render(request, 'feedbacks/monitorOpenfeedback.html', {
        'feedback': feedback,

    })

def monitorRespostaFeedback(request, user_id, feedback_id):
    submitted = False
    context = {}
    if request.POST:
        form = FeedbacksRespostaForm(request.POST, request.FILES)

        if form.is_valid():
            Feedbackform = form.save(commit=False)
            ultimo_feedback = get_object_or_404(Feedbacks, fee_id=feedback_id)

            Feedbackform.fee_titulo = ultimo_feedback.fee_titulo
            Feedbackform.fee_emissor = request.user
            Feedbackform.fee_anterior = ultimo_feedback.fee_id
            Feedbackform.fee_acompanhamento = ultimo_feedback.fee_acompanhamento
            if ultimo_feedback.fee_inicial:
                Feedbackform.fee_inicial = ultimo_feedback.fee_inicial
            else:
                Feedbackform.fee_inicial = ultimo_feedback.fee_id
            Feedbackform.fee_new = True

            Feedbackform.save()
            print(Feedbackform.fee_id)
            ultimo_feedback.fee_proximo = Feedbackform.fee_id
            ultimo_feedback.save()
            messages.success(request, "Feedback de resposta enviado com sucesso!")
            return redirect('monitorFeedbackAll', user_id)

        else:
            form = FeedbacksRespostaForm()
            return HttpResponseRedirect('monitorRespostaFeedback?submitted=True')
    else:
        form = FeedbacksRespostaForm()
        if 'submitted' in request.GET:
            submitted = True

    context['form'] = form
    context['submitted'] = submitted

    return render(request, 'feedbacks/monitorRespostaFeedback.html', context)

def monitorMarcarComoLido(request, feedback_id):
    feedback = Feedbacks.objects.filter(fee_id=feedback_id)
    feedback.fee_new = False
    feedback.save()
    user = get_object_or_404(CustomUser, id=request.user.id)
    messages.success(request, "Feedback marcado como lido!.")
    return redirect('monitorFeedbackAll', user.id)

#TUTOR-FEEDBACK
def tutorFeedback(request, user_id):
    submitted = False
    context = {}

    user = get_object_or_404(CustomUser, id=user_id)
    if request.POST:
        form = FeedbacksTutorForm(user, request.POST, request.FILES)

        if form.is_valid():
            Feedbackform = form.save(commit=False)
            Feedbackform.fee_emissor = user
            Feedbackform.fee_new = True
            Feedbackform.save()
            messages.success(request, "Feedback iniciado com sucesso!")
            return redirect('tutorFeedbackAll', user_id)
        else:
            form = FeedbacksTutorForm(user)
            return HttpResponseRedirect('tutorFeedback?submitted=True')
    else:
        form = FeedbacksTutorForm(user)
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted

    return render (request, 'feedbacks/tutorFeedback.html', context)

def tutorFeedbackAll(request, user_id):

    user = get_object_or_404(CustomUser, id=user_id)
    tutor = get_object_or_404(Tutor, tut_cpf=user.username)
    tutorias = AcompanhamentoTutores.objects.filter(AsTut_tutor=tutor)
    acompanhamentos = Acompanhamentos.objects.filter(aco_id__in=[t.AsTut_acompanhamento.aco_id for t in tutorias.all()])
    feedback = Feedbacks.objects.order_by('-fee_id').filter(fee_acompanhamento__in=[a.aco_id for a in acompanhamentos.all()], fee_anterior=None )

    paginator = Paginator(feedback, 7)
    page = request.GET.get('p')
    feedback = paginator.get_page(page)

    return render(request, 'feedbacks/tutorFeedbackAll.html', {
        'feedback': feedback,
        'acompanhamentos': acompanhamentos,
    })

def tutorOpenAllfeedback(request, user_id, feedback_id):

    user = get_object_or_404(CustomUser, id=user_id)
    tutor = get_object_or_404(Tutor, tut_cpf=user.username)
    tutorias = AcompanhamentoTutores.objects.filter(AsTut_tutor=tutor)
    feedbackInicial = get_object_or_404(Feedbacks, fee_id=feedback_id)
    acompanhamentos = Acompanhamentos.objects.filter(aco_id__in=[t.AsTut_acompanhamento.aco_id for t in tutorias.all()])
    list_feedback = Feedbacks.objects.filter(fee_acompanhamento__in=[a.aco_id for a in acompanhamentos.all()])

    feedback = []
    f0 = feedbackInicial
    feedback.append(f0)
    ultimo_feedback = None
    for f1 in list_feedback:
        if f1.fee_anterior == f0.fee_id:
            feedback.append(f1)
            f0=f1
            if f1.fee_proximo == None:
                ultimo_feedback = f1
                break
    feedback = reversed(feedback)
    return render(request, 'feedbacks/tutorOpenAllfeedback.html', {
        'feedback': feedback,
        'ultimo_feedback': ultimo_feedback,
        'feedbackInicial': feedbackInicial
    })
def tutorOpenfeedback(request, user_id, feedback_id):
    feedback = get_object_or_404(Feedbacks, fee_id=feedback_id)

    if feedback.fee_proximo != None:
        return tutorOpenAllfeedback(request, user_id, feedback_id)
    return render(request, 'feedbacks/tutorOpenfeedback.html', {
        'feedback': feedback,

    })

def tutorRespostaFeedback(request, user_id, feedback_id):
    submitted = False
    context = {}
    if request.POST:
        form = FeedbacksRespostaForm(request.POST, request.FILES)

        if form.is_valid():
            Feedbackform = form.save(commit=False)
            ultimo_feedback = get_object_or_404(Feedbacks, fee_id=feedback_id)

            Feedbackform.fee_titulo = ultimo_feedback.fee_titulo
            Feedbackform.fee_emissor = request.user
            Feedbackform.fee_anterior = ultimo_feedback.fee_id
            Feedbackform.fee_acompanhamento = ultimo_feedback.fee_acompanhamento
            if ultimo_feedback.fee_inicial:
                Feedbackform.fee_inicial = ultimo_feedback.fee_inicial
            else:
                Feedbackform.fee_inicial = ultimo_feedback.fee_id
            Feedbackform.fee_new = True

            Feedbackform.save()
            print(Feedbackform.fee_id)
            ultimo_feedback.fee_proximo = Feedbackform.fee_id
            ultimo_feedback.save()
            messages.success(request, "Feedback de resposta enviado com sucesso!")
            return redirect('tutorFeedbackAll', user_id)

        else:
            form = FeedbacksRespostaForm()
            return HttpResponseRedirect('tutorRespostaFeedback?submitted=True')
    else:
        form = FeedbacksRespostaForm()
        if 'submitted' in request.GET:
            submitted = True

    context['form'] = form
    context['submitted'] = submitted

    return render(request, 'feedbacks/tutorRespostaFeedback.html', context)

def tutorMarcarComoLido(request, feedback_id):
    feedback = Feedbacks.objects.filter(fee_id=feedback_id)
    feedback.fee_new = False
    feedback.save()
    user = get_object_or_404(CustomUser, id=request.user.id)
    messages.success(request, "Feedback marcado como lido!.")
    return redirect('tutorFeedbackAll', user.id)