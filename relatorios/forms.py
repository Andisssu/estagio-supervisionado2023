from django import forms
from django.forms import ModelForm
from .models import RelatoriosMon, RelatoriosTut

class RelatoriosMonForm(ModelForm):

    class Meta:
        model = RelatoriosMon
        fields = ('relM_titulo', 'relM_arquivo', 'relM_monitoria')
        labels = {
            'relM_titulo': 'Digite o título do relatório',
            'relM_arquivo': 'Anexe um arquivo abaixo',
            'relM_monitoria': 'Defina a monitoria relacionada',
        }
        widgets = {
            'relM_titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Titulo'}),
            'relM_arquivo': forms.FileInput(attrs={'class':'form-control'}),
            'relM_monitoria': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Monitoria'}),
        }

class RelatoriosTutForm(ModelForm):

    class Meta:
        model = RelatoriosTut
        fields = ('relT_titulo', 'relT_arquivo', 'relT_tutoria')
        labels = {
            'relT_titulo': 'Digite o título do aviso',
            'relT_arquivo': 'Anexe um arquivo abaixo',
            'relT_tutoria': 'Defina a tutoria relacionada',
        }
        widgets = {
            'relT_titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Titulo'}),
            'relT_arquivo': forms.FileInput(attrs={'class':'form-control'}),
            'relT_tutoria': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Tutoria'}),
        }