from django import forms
from django.forms import ModelForm
from .models import Avisos
from portal import settings

class AvisosForm(ModelForm):

    class Meta:
        model = Avisos
        fields = ['avi_titulo', 'avi_descricao', 'avi_arquivos', 'avi_mostrar']

        labels = {
            'avi_titulo': 'Digite o nome do aviso',
            'avi_descricao': 'Digite a descriçâo do aviso',
            'avi_arquivos': 'Anexe um arquivo abaixo',
            'avi_mostrar': 'Defina o estado de visualização',
        }
        widgets = {
            'avi_titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Titulo'}),
            'avi_descricao': forms.Textarea(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Descrição', 'rows': '10'}),
            'avi_arquivos': forms.FileInput(attrs={'class':'form-control'}),
            'avi_mostrar': forms.CheckboxInput(attrs={'class':'form-control'}),
        }
