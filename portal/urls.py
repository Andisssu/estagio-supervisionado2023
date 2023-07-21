"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', include('authentication.urls')), # Rota para a URL raiz
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('acompanhamentos/', include('acompanhamentos.urls')),
    path('avisos/', include('avisos.urls')),
    path('feedbacks/', include('feedbacks.urls')),
    path('membros/', include('membros.urls')),
    path('relatorios/', include('relatorios.urls')),
    path('sistema/', include('sistema.urls')),
    path('404', TemplateView.as_view(template_name="404.html")),
    path('index', TemplateView.as_view(template_name="index.html")),
    path('auth/', include('authentication.urls')),
]
