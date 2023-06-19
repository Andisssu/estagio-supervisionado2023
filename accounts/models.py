from django.db import models
from membros.models import Administrador, AlunoPcd, Monitor, Tutor, Interprete
from django import forms

class FormAdministrador(forms.ModelForm):
    class Meta:
        model = Administrador
        exclude = ()

# Create your models here.

class FormAlunoPcd(forms.ModelForm):
    class Meta:
        model = AlunoPcd
        exclude = ('alu_id',)

    labels = {
        'alu_nome': 'Digite o nome',
        'alu_cpf': 'Digite o CPF',
        'alu_genero': 'Defina o genero',
        'alu_email_pessoal': 'Digite o email pessoal',
        'alu_email_institucional': 'Digite o email institucional',
        'alu_telefone': 'Digite o contato',
        'alu_endereco_cep': 'Digite o CEP do endereco',
        'alu_endereco_descricao': 'Digite o endereco',
        'alu_endereco_cidade': 'Defina a cidade',
        'alu_matricula': 'Digite a matricula',
        'alu_deficiencias': 'Cite as deficiencias',
        'alu_curso': 'Defina o curso',
        'alu_periodo_academico': 'Defina o periodo academico',
        'alu_data_nascimento': 'Defina a data de nascimento',
    }
    widgets = {
        'alu_nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
        'alu_cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF'}),
        'alu_genero': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Genero'}),
        'alu_email_pessoal': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email pessoal'}),
        'alu_email_institucional': forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email Institucional'}),
        'alu_telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
        'alu_matricula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Matricula'}),
        'alu_deficiencias': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Deficiencias'}),
        'alu_curso': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Curso'}),
        'alu_endereco_cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CEP'}),
        'alu_endereco_descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereco'}),
        'alu_endereco_cidade': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
        'alu_periodo_academico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Periodo'}),
        'alu_data_nascimento': forms.DateInput(attrs={'class': 'date', 'placeholder': '____-__-__'})
    }


class FormMonitor(forms.ModelForm):
    class Meta:
        model = Monitor
        exclude = ('mon_id',)

class FormTutor(forms.ModelForm):
    class Meta:
        model = Tutor
        exclude = ('tut_id',)


class FormInterprete(forms.ModelForm):
    class Meta:
        model = Interprete
        exclude = ('int_id',)