from django import forms
from django.forms import ModelForm
from .models import Acompanhamentos, AcompanhamentoDisciplinas, AcompanhamentoMonitores,\
    AcompanhamentoTutores, AcompanhamentoInterpretes, HorariosDisciplina

class AcompanhamentosForm(ModelForm):

    class Meta:
        model = Acompanhamentos
        fields = ('aco_semestre', 'aco_inicio', 'aco_fim', 'aco_aluno_pcd')
        labels = {
            'aco_semestre': 'Digite o semestre do acompanhamento',
            'aco_inicio': 'Defina a data inicial do acompanhamento',
            'aco_fim': 'Defina a data final do acompanhamento',
            'aco_aluno_pcd': 'Defina o aluno acompanhado',
        }
        widgets = {
            'aco_semestre': forms.TextInput(attrs={'class':'form-control', 'placeholder': '____._'}),
            'aco_inicio': forms.DateInput(attrs={'class':'form-control'}),
            'aco_fim': forms.DateInput(attrs={'class':'form-control'}),
            'aco_aluno_pcd': forms.Select(attrs={'class':'form-control'}),
        }

class AcoDisciplinasForm(ModelForm):

    class Meta:
        model = AcompanhamentoDisciplinas
        fields = ('AsDis_disciplina', 'AsDis_acompanhamento')
        labels = {
            'AsDis_disciplina': 'Selecione a disciplina',
            'AsDis_acompanhamento': 'Defina o acompanhamento relacionado',
        }
        widgets = {
            'AsDis_disciplina': forms.Select(attrs={'class': 'form-control'}),
            'AsDis_acompanhamento': forms.Select(attrs={'class': 'form-control'}),
        }

class AcoMonitoriasForm(ModelForm):

    class Meta:
        model = AcompanhamentoMonitores
        fields = ('AsMon_inicio', 'AsMon_fim', 'AsMon_monitor', 'AsMon_acompanhamento')
        labels = {
            'AsMon_inicio': 'Defina a data inicial da monitoria',
            'AsMon_fim': 'Defina a data final da monitoria',
            'AsMon_monitor': 'Defina o monitor',
            'AsMon_acompanhamento': 'Defina o acompanhamento relacionado',
        }
        widgets = {
            'AsMon_inicio': forms.DateInput(attrs={'class':'form-control'}),
            'AsMon_fim': forms.DateInput(attrs={'class':'form-control'}),
            'AsMon_monitor': forms.Select(attrs={'class': 'form-control'}),
            'AsMon_acompanhamento': forms.Select(attrs={'class': 'form-control'}),
        }

class AcoTutoriasForm(ModelForm):

    class Meta:
        model = AcompanhamentoTutores
        fields = ('AsTut_inicio', 'AsTut_fim', 'AsTut_tutor', 'AsTut_acompanhamento')
        labels = {
            'AsTut_inicio': 'Defina a data inicial da tutoria',
            'AsTut_fim': 'Defina a data final da tutoria',
            'AsTut_tutor': 'Defina o tutor',
            'AsTut_acompanhamento': 'Defina o acompanhamento relacionado',
        }
        widgets = {
            'AsTut_inicio': forms.DateInput(attrs={'class':'form-control'}),
            'AsTut_fim': forms.DateInput(attrs={'class':'form-control'}),
            'AsTut_tutor': forms.Select(attrs={'class': 'form-control'}),
            'AsTut_acompanhamento': forms.Select(attrs={'class': 'form-control'}),
        }

class AcoInterpretacoesForm(ModelForm):

    class Meta:
        model = AcompanhamentoInterpretes
        fields = ('AsInt_inicio', 'AsInt_fim', 'AsInt_interprete', 'AsInt_acompanhamento')
        labels = {
            'AsInt_inicio': 'Defina a data inicial da interpretação',
            'AsInt_fim': 'Defina a data final da interpretação',
            'AsInt_interprete': 'Defina o interprete',
            'AsInt_acompanhamento': 'Defina o acompanhamento relacionado',
        }
        widgets = {
            'AsInt_inicio': forms.DateInput(attrs={'class':'form-control'}),
            'AsInt_fim': forms.DateInput(attrs={'class':'form-control'}),
            'AsInt_interprete': forms.Select(attrs={'class': 'form-control'}),
            'AsInt_acompanhamento': forms.Select(attrs={'class': 'form-control'}),
        }

class HorDisciplinaForm(ModelForm):

    class Meta:
        model = HorariosDisciplina
        fields = ('HoDis_dia', 'HoDis_inicio', 'HoDis_fim', 'HoDis_disciplina')
        labels = {
            'HoDis_dia': 'Defina o dia',
            'HoDis_inicio': 'Defina o horário de início',
            'HoDis_fim': 'Defina o horário de término',
            'HoDis_disciplina': 'Defina a disciplina',
        }
