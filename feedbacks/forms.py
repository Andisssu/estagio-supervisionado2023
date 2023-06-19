from django.shortcuts import get_object_or_404
from django import forms
from django.forms import ModelForm
from .models import Feedbacks
from acompanhamentos.models import Acompanhamentos, AcompanhamentoMonitores, AcompanhamentoTutores
from membros.models import Monitor, Tutor, CustomUser

class FeedbacksForm(ModelForm):

    class Meta:
        model = Feedbacks
        fields = ('fee_titulo', 'fee_descricao', 'fee_arquivo')
        labels = {
            'fee_titulo': 'Escolha o tipo de Feedback',
            'fee_descricao': 'Digite a mensagem de feedback.',
            'fee_arquivo': 'Anexe um arquivo abaixo',

        }
        widgets = {
            'fee_titulo': forms.Select(attrs={'class':'form-control', 'placeholder': 'Titulo'}),
            'fee_descricao': forms.Textarea(attrs={'class':'form-control', 'rows':5, 'placeholder': 'Descricao'}),
            'fee_arquivo': forms.FileInput(attrs={'class':'form-control'}),
        }
class FeedbacksRespostaForm(ModelForm):

    class Meta:
        model = Feedbacks
        fields = ('fee_descricao', 'fee_arquivo',  'fee_anterior',  'fee_proximo')
        labels = {
            'fee_descricao': 'Digite a mensagem de feedback.',
            'fee_arquivo': 'Anexe um arquivo abaixo',
        }
        widgets = {
            'fee_descricao': forms.Textarea(attrs={'class':'form-control', 'rows':5, 'placeholder': 'Descricao'}),
            'fee_arquivo': forms.FileInput(attrs={'class':'form-control'}),
            'fee_anterior': forms.TextInput(attrs={'type': 'hidden'}),
            'fee_proximo': forms.TextInput(attrs={'type': 'hidden'}),
        }

class FeedbacksMonitorForm(ModelForm):
    def __init__(self, user=None, *args, **kwargs):
        monitor = get_object_or_404(Monitor ,mon_cpf=user.username)
        monitorias = AcompanhamentoMonitores.objects.filter(AsMon_monitor=monitor)
        self.acompanhamentos = Acompanhamentos.objects.filter(aco_id__in=[m.AsMon_acompanhamento.aco_id for m in monitorias.all()])
        super(FeedbacksMonitorForm, self).__init__(*args, **kwargs)
        self.fields['fee_acompanhamento'].queryset = self.acompanhamentos

    class Meta:
        model = Feedbacks
        fields = ('fee_titulo', 'fee_descricao', 'fee_arquivo', 'fee_acompanhamento')
        labels = {
            'fee_titulo': 'Escolha o tipo de Feedback',
            'fee_descricao': 'Digite a mensagem de feedback',
            'fee_arquivo': 'Anexe um arquivo abaixo',
            'fee_acompanhamento': 'Selecione o acompanhamento relacionado',

        }
        widgets = {
            'fee_titulo': forms.Select(attrs={'class':'form-control', 'placeholder': 'Titulo'}),
            'fee_descricao': forms.Textarea(attrs={'class':'form-control', 'rows':5, 'placeholder': 'Descricao'}),
            'fee_arquivo': forms.FileInput(attrs={'class':'form-control'}),
            'fee_acompanhamento': forms.Select(attrs={'class': 'form-control'}),
        }

class FeedbacksTutorForm(ModelForm):
    def __init__(self, user=None, *args, **kwargs):
        tutor = get_object_or_404(Tutor, tut_cpf=user.username)
        tutorias = AcompanhamentoTutores.objects.filter(AsTut_tutor=tutor)
        self.acompanhamentos = Acompanhamentos.objects.filter(aco_id__in=[t.AsTut_acompanhamento.aco_id for t in tutorias.all()])
        super(FeedbacksTutorForm, self).__init__(*args, **kwargs)
        self.fields['fee_acompanhamento'].queryset = self.acompanhamentos

    class Meta:
        model = Feedbacks
        fields = ('fee_titulo', 'fee_descricao', 'fee_arquivo', 'fee_acompanhamento')
        labels = {
            'fee_titulo': 'Escolha o tipo de Feedback',
            'fee_descricao': 'Digite a mensagem de feedback',
            'fee_arquivo': 'Anexe um arquivo abaixo',
            'fee_acompanhamento': 'Selecione o acompanhamento relacionado',

        }
        widgets = {
            'fee_titulo': forms.Select(attrs={'class':'form-control', 'placeholder': 'Titulo'}),
            'fee_descricao': forms.Textarea(attrs={'class':'form-control', 'rows':5, 'placeholder': 'Descricao'}),
            'fee_arquivo': forms.FileInput(attrs={'class':'form-control'}),
            'fee_acompanhamento': forms.Select(attrs={'class': 'form-control'}),
        }