import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from .models import Avisos
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import AvisosForm
from membros.models import AlunoPcd, Administrador
import mimetypes
import pickle

def baixarFileAviso(request, filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = str(filename)
    filepath = BASE_DIR + '\\uploads\\' + filename
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def aviIndex(request):
    avisos = Avisos.objects.order_by('-avi_id').filter(
        avi_mostrar = True
    )
    paginator = Paginator(avisos, 10)

    page = request.GET.get('p')
    avisos = paginator.get_page(page)
    return render(request, 'avisos/aviIndex.html', {
        'avisos': avisos
    })

def adicionarAviso(request):

    context = {}
    if request.POST:
        form = AvisosForm(request.POST, request.FILES)
        if form.is_valid():
            avisoForm = form.save(commit=False)
            administrador = get_object_or_404(Administrador, adm_cpf=request.user.username)
            avisoForm.avi_administrador = administrador
            avisoForm.save()
            messages.success(request, "Aviso enviado com sucesso!")
            return redirect('aviIndex')
        else:
            form = AvisosForm(request.POST)
            messages.error(request, "As informações inseridas são inválidas! Tente novamente.")
    else:
        form = AvisosForm()
    context['form'] = form
    return render(request, 'avisos/adicionarAviso.html', context)

def buscarAviso(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            avisos = Avisos.objects.order_by('-avi_id').filter(Q(avi_titulo__icontains=searched) | Q(avi_descricao__icontains=searched) )
        else:
            avisos = None

        return render(request, 'avisos/buscarAviso.html', {
            'searched': searched,
            'avisos': avisos
        })
    else:
        return render(request, 'avisos/buscarAviso.html', {

        })

def aviso(request, aviso_id):
    aviso = get_object_or_404(Avisos, avi_id=aviso_id)
    if not aviso.avi_mostrar:
        raise Http404()

    return render(request, 'avisos/aviso.html', {
        'aviso': aviso
    })

def atualizarAviso(request, aviso_id):
    aviso = get_object_or_404(Avisos, avi_id=aviso_id)
    if not aviso.avi_mostrar:
        raise Http404()

    if request.method == 'POST':
        form = AvisosForm(request.POST or None, request.FILES, instance=aviso)
        if form.is_valid():
            form.save()
            return redirect('aviIndex')
    else:
        form = AvisosForm(instance=aviso)

    return render(request, 'avisos/atualizarAviso.html', {
        'aviso': aviso,
        'form': form
    })

def deletarAviso(request, aviso_id):
    aviso = get_object_or_404(Avisos, avi_id=aviso_id)
    arquivo_nome = aviso.avi_arquivos
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = BASE_DIR + '\\uploads\\' + str(arquivo_nome)
    aviso.delete()
    try:
        os.remove(filepath)
    except:
        pass
    return redirect('aviIndex')



#ALUNO==============================================================================================
def aviIndexAluno(request):
    avisos = Avisos.objects.order_by('-avi_id').filter(
        avi_mostrar = True
    )
    paginator = Paginator(avisos, 10)

    page = request.GET.get('p')
    avisos = paginator.get_page(page)
    return render(request, 'avisos/aviIndexAluno.html', {
        'avisos': avisos
    })

def avisoAluno(request, aviso_id):
    aviso = get_object_or_404(Avisos, avi_id=aviso_id)
    if not aviso.avi_mostrar:
        raise Http404()

    return render(request, 'avisos/avisoAluno.html', {
        'aviso': aviso
    })


def buscarAvisoAluno(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            avisos = Avisos.objects.order_by('-avi_id').filter(Q(avi_titulo__icontains=searched) | Q(avi_descricao__icontains=searched) )
        else:
            avisos = None

        return render(request, 'avisos/buscarAvisoAluno.html', {
            'searched': searched,
            'avisos': avisos
        })
    else:
        return render(request, 'avisos/buscarAvisoAluno.html', {

        })

#MONITOR============================================================================================
def aviIndexMonitor(request):
    avisos = Avisos.objects.order_by('-avi_id').filter(
        avi_mostrar = True
    )
    paginator = Paginator(avisos, 10)

    page = request.GET.get('p')
    avisos = paginator.get_page(page)
    return render(request, 'avisos/aviIndexMonitor.html', {
        'avisos': avisos
    })

def avisoMonitor(request, aviso_id):
    aviso = get_object_or_404(Avisos, avi_id=aviso_id)
    if not aviso.avi_mostrar:
        raise Http404()

    return render(request, 'avisos/avisoMonitor.html', {
        'aviso': aviso
    })


def buscarAvisoMonitor(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            avisos = Avisos.objects.order_by('-avi_id').filter(Q(avi_titulo__icontains=searched) | Q(avi_descricao__icontains=searched) )
        else:
            avisos = None

        return render(request, 'avisos/buscarAvisoMonitor.html', {
            'searched': searched,
            'avisos': avisos
        })
    else:
        return render(request, 'avisos/buscarAvisoMonitor.html', {

        })

#TUTOR==============================================================================================
def aviIndexTutor(request):
    avisos = Avisos.objects.order_by('-avi_id').filter(
        avi_mostrar = True
    )
    paginator = Paginator(avisos, 10)

    page = request.GET.get('p')
    avisos = paginator.get_page(page)
    return render(request, 'avisos/aviIndexTutor.html', {
        'avisos': avisos
    })

def avisoTutor(request, aviso_id):
    aviso = get_object_or_404(Avisos, avi_id=aviso_id)
    if not aviso.avi_mostrar:
        raise Http404()

    return render(request, 'avisos/avisoTutor.html', {
        'aviso': aviso
    })


def buscarAvisoTutor(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            avisos = Avisos.objects.order_by('-avi_id').filter(Q(avi_titulo__icontains=searched) | Q(avi_descricao__icontains=searched) )
        else:
            avisos = None

        return render(request, 'avisos/buscarAvisoTutor.html', {
            'searched': searched,
            'avisos': avisos
        })
    else:
        return render(request, 'avisos/buscarAvisoTutor.html', {

        })

#INTERPRETE=========================================================================================
def aviIndexInterprete(request):
    avisos = Avisos.objects.order_by('-avi_id').filter(
        avi_mostrar = True
    )
    paginator = Paginator(avisos, 10)

    page = request.GET.get('p')
    avisos = paginator.get_page(page)
    return render(request, 'avisos/aviIndexInterprete.html', {
        'avisos': avisos
    })

def avisoInterprete(request, aviso_id):
    aviso = get_object_or_404(Avisos, avi_id=aviso_id)
    if not aviso.avi_mostrar:
        raise Http404()

    return render(request, 'avisos/avisoInterprete.html', {
        'aviso': aviso
    })


def buscarAvisoInterprete(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            avisos = Avisos.objects.order_by('-avi_id').filter(Q(avi_titulo__icontains=searched) | Q(avi_descricao__icontains=searched) )
        else:
            avisos = None

        return render(request, 'avisos/buscarAvisoInterprete.html', {
            'searched': searched,
            'avisos': avisos
        })
    else:
        return render(request, 'avisos/buscarAvisoInterprete.html', {

        })