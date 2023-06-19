from django.shortcuts import render
from django.http import HttpResponse

def ola(request):
    return render(request, 'sistema/ola.html')
