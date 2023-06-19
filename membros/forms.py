from django import forms
from django.forms import ModelForm
from .models import AlunoPcd, Monitor, Tutor, Interprete, Administrador

class AdminsForm(ModelForm):

    class Meta:
        model = Administrador
        fields = ('adm_nome', 'adm_cpf', 'adm_email')
        labels = {
            'adm_nome': 'Digite o nome',
            'adm_cpf': 'Digite o CPF',
            'adm_email': 'Digite o email'
        }
        widgets = {
            'adm_nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'adm_cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF'}),
            'adm_email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'}),
        }

class AlunosForm(ModelForm):

    class Meta:
        model = AlunoPcd
        fields = ('alu_nome', 'alu_cpf', 'alu_genero', 'alu_email_pessoal', 'alu_email_institucional', 'alu_telefone',
                  'alu_endereco_cep', 'alu_endereco_descricao', 'alu_endereco_cidade', 'alu_matricula', 'alu_deficiencias', 'alu_curso',
                  'alu_periodo_academico', 'alu_data_nascimento')
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
            'alu_nome': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nome'}),
            'alu_cpf': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'CPF'}),
            'alu_genero': forms.Select(attrs={'class':'form-control', 'placeholder': 'Genero'}),
            'alu_email_pessoal': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email pessoal'}),
            'alu_email_institucional': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email Institucional'}),
            'alu_telefone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Telefone'}),
            'alu_matricula': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Matricula'}),
            'alu_deficiencias': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Deficiencias'}),
            'alu_curso': forms.Select(attrs={'class':'form-control', 'placeholder': 'Curso'}),
            'alu_endereco_cep': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'CEP'}),
            'alu_endereco_descricao': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Endereco'}),
            'alu_endereco_cidade': forms.Select(attrs={'class':'form-control', 'placeholder': 'Cidade'}),
            'alu_periodo_academico': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Periodo'}),
            'alu_data_nascimento': forms.DateInput(attrs={'class':'date', 'placeholder': '____-__-__'}),
        }

class AtualizarAlunosForm(ModelForm):
    class Meta:
        model = AlunoPcd
        fields = ('alu_email_pessoal', 'alu_email_institucional', 'alu_telefone',
                  'alu_endereco_cep', 'alu_endereco_descricao', 'alu_endereco_cidade')
        labels = {
            'alu_email_pessoal': 'Digite o email pessoal',
            'alu_email_institucional': 'Digite o email institucional',
            'alu_telefone': 'Digite o contato',
            'alu_endereco_cep': 'Digite o CEP do endereco',
            'alu_endereco_descricao': 'Digite o endereco',
            'alu_endereco_cidade': 'Defina a cidade',
        }
        widgets = {
            'alu_email_pessoal': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email pessoal'}),
            'alu_email_institucional': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email Institucional'}),
            'alu_telefone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Telefone'}),
            'alu_endereco_cep': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'CEP'}),
            'alu_endereco_descricao': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Endereco'}),
            'alu_endereco_cidade': forms.Select(attrs={'class':'form-control', 'placeholder': 'Cidade'}),
        }

class MonitoresForm(ModelForm):

    class Meta:
        model = Monitor
        fields = ('mon_nome', 'mon_cpf', 'mon_genero', 'mon_email_pessoal', 'mon_email_institucional', 'mon_telefone',
                  'mon_endereco_cep', 'mon_endereco_descricao', 'mon_endereco_cidade', 'mon_matricula',
                  'mon_curso', 'mon_periodo_academico')
        labels = {
            'mon_nome': 'Digite o nome',
            'mon_cpf': 'Digite o CPF',
            'mon_genero': 'Defina o genero',
            'mon_email_pessoal': 'Digite o email pessoal',
            'mon_email_institucional': 'Digite o email institucional',
            'mon_telefone': 'Digite o contato',
            'mon_endereco_cep': 'Digite o CEP do endereco',
            'mon_endereco_descricao': 'Digite o endereco',
            'mon_endereco_cidade': 'Defina a cidade',
            'mon_matricula': 'Digite a matricula',
            'mon_curso': 'Defina o curso',
            'mon_periodo_academico': 'Defina o periodo academico',
        }
        widgets = {
            'mon_nome': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nome'}),
            'mon_cpf': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'CPF'}),
            'mon_genero': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gênero'}),
            'mon_email_pessoal': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email pessoal'}),
            'mon_email_institucional': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email Institucional'}),
            'mon_telefone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Telefone'}),
            'mon_endereco_cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CEP'}),
            'mon_endereco_descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereco'}),
            'mon_endereco_cidade': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
            'mon_matricula': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Matricula'}),
            'mon_curso': forms.Select(attrs={'class':'form-control', 'placeholder': 'Curso'}),
            'mon_periodo_academico': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Periodo'}),
        }

class AtualizarMonitoresForm(ModelForm):

    class Meta:
        model = Monitor
        fields = ('mon_email_pessoal', 'mon_email_institucional', 'mon_telefone',
                  'mon_endereco_cep', 'mon_endereco_descricao', 'mon_endereco_cidade')
        labels = {
            'mon_email_pessoal': 'Digite o email pessoal',
            'mon_email_institucional': 'Digite o email institucional',
            'mon_telefone': 'Digite o contato',
            'mon_endereco_cep': 'Digite o CEP do endereco',
            'mon_endereco_descricao': 'Digite o endereco',
            'mon_endereco_cidade': 'Defina a cidade',
        }
        widgets = {
            'mon_email_pessoal': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email pessoal'}),
            'mon_email_institucional': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email Institucional'}),
            'mon_telefone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Telefone'}),
            'mon_endereco_cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CEP'}),
            'mon_endereco_descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereco'}),
            'mon_endereco_cidade': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
        }

class TutoresForm(ModelForm):

    class Meta:
        model = Tutor
        fields = ('tut_nome', 'tut_cpf', 'tut_genero', 'tut_email_pessoal', 'tut_email_institucional', 'tut_telefone',
                  'tut_endereco_cep', 'tut_endereco_descricao', 'tut_endereco_cidade', 'tut_matricula',
                  'tut_curso', 'tut_periodo_academico')
        labels = {
            'tut_nome': 'Digite o nome',
            'tut_cpf': 'Digite o CPF',
            'tut_genero': 'Defina o genero',
            'tut_email_pessoal': 'Digite o email pessoal',
            'tut_email_institucional': 'Digite o email institucional',
            'tut_telefone': 'Digite o contato',
            'tut_endereco_cep': 'Digite o CEP do endereco',
            'tut_endereco_descricao': 'Digite o endereco',
            'tut_endereco_cidade': 'Defina a cidade',
            'tut_matricula': 'Digite a matricula',
            'tut_curso': 'Defina o curso',
            'tut_periodo_academico': 'Defina o periodo academico',
        }
        widgets = {
            'tut_nome': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nome'}),
            'tut_cpf': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'CPF'}),
            'tut_genero': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gênero'}),
            'tut_email_pessoal': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email pessoal'}),
            'tut_email_institucional': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email Institucional'}),
            'tut_telefone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Telefone'}),
            'tut_endereco_cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CEP'}),
            'tut_endereco_descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereco'}),
            'tut_endereco_cidade': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
            'tut_matricula': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Matricula'}),
            'tut_curso': forms.Select(attrs={'class':'form-control', 'placeholder': 'Curso'}),
            'tut_periodo_academico': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Periodo'}),
        }

class AtualizarTutoresForm(ModelForm):

    class Meta:
        model = Tutor
        fields = ('tut_email_pessoal', 'tut_email_institucional', 'tut_telefone',
                  'tut_endereco_cep', 'tut_endereco_descricao', 'tut_endereco_cidade')
        labels = {
            'tut_email_pessoal': 'Digite o email pessoal',
            'tut_email_institucional': 'Digite o email institucional',
            'tut_telefone': 'Digite o contato',
            'tut_endereco_cep': 'Digite o CEP do endereco',
            'tut_endereco_descricao': 'Digite o endereco',
            'tut_endereco_cidade': 'Defina a cidade',
        }
        widgets = {
            'tut_email_pessoal': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email pessoal'}),
            'tut_email_institucional': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email Institucional'}),
            'tut_telefone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Telefone'}),
            'tut_endereco_cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CEP'}),
            'tut_endereco_descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereco'}),
            'tut_endereco_cidade': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
        }

class InterpretesForm(ModelForm):

    class Meta:
        model = Interprete
        fields = ('int_nome', 'int_cpf', 'int_genero', 'int_email_pessoal', 'int_email_institucional', 'int_telefone')
        labels = {
            'int_nome': 'Digite o nome',
            'int_cpf': 'Digite o CPF',
            'int_genero': 'Defina o genero',
            'int_email_pessoal': 'Digite o email pessoal',
            'int_email_institucional': 'Digite o email institucional',
            'int_telefone': 'Digite o contato',
        }
        widgets = {
            'int_nome': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nome'}),
            'int_cpf': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'CPF'}),
            'int_genero': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gênero'}),
            'int_email_pessoal': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email pessoal'}),
            'int_email_institucional': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email Institucional'}),
            'int_telefone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Telefone'}),
        }

class AtualizarInterpretesForm(ModelForm):

    class Meta:
        model = Interprete
        fields = ('int_email_pessoal', 'int_email_institucional', 'int_telefone')
        labels = {
            'int_email_pessoal': 'Digite o email pessoal',
            'int_email_institucional': 'Digite o email institucional',
            'int_telefone': 'Digite o contato',
        }
        widgets = {
            'int_email_pessoal': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email pessoal'}),
            'int_email_institucional': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email Institucional'}),
            'int_telefone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Telefone'}),
        }