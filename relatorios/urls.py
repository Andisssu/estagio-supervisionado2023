from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('baixarFileRelatorio/<str:filename>', views.baixarFileRelatorio, name='baixarFileRelatorio'),
    #ADMIN
    path('ativaVerificadoM/<int:relM_id>', views.ativaVerificadoM, name='ativaVerificadoM'),
    path('desativaVerificadoM/<int:relM_id>', views.desativaVerificadoM, name='desativaVerificadoM'),
    path('ativaVerificadoT/<int:relT_id>', views.ativaVerificadoT, name='ativaVerificadoT'),
    path('desativaVerificadoT/<int:relT_id>', views.desativaVerificadoT, name='desativaVerificadoT'),
    path('relMIndex', views.relMIndex, name='relMIndex'),
    path('relTIndex', views.relTIndex, name='relTIndex'),
    path('relatorioM/<int:relatorioM_id>', views.relatorioM, name='relatorioM'),
    path('relatorioT/<int:relatorioT_id>', views.relatorioT, name='relatorioT'),
    path('buscarRelatorioM', views.buscarRelatorioM, name='buscarRelatorioM'),
    path('buscarRelatorioT', views.buscarRelatorioT, name='buscarRelatorioT'),
    path('deletarRelatorioM/<int:relM_id>', views.deletarRelatorioM, name='deletarRelatorioM'),
    path('deletarRelatorioT/<int:relT_id>', views.deletarRelatorioT, name='deletarRelatorioT'),

    #MONITOR_TUTOR
    path('ajudaVerificadoM', views.ajudaVerificadoM, name='ajudaVerificadoM'),
    path('ajudaVerificadoT', views.ajudaVerificadoT, name='ajudaVerificadoT'),
    path('relMIndexMonitor/<int:user_id>', views.relMIndexMonitor, name='relMIndexMonitor'),
    path('relTIndexTutor/<int:user_id>', views.relTIndexTutor, name='relTIndexTutor'),
    path('adicionarRelatorioMonitor', views.adicionarRelatorioMonitor, name='adicionarRelatorioMonitor'),
    path('adicionarRelatorioTutor', views.adicionarRelatorioTutor, name='adicionarRelatorioTutor'),
    path('buscarRelatorioMonitor/<int:user_id>', views.buscarRelatorioMonitor, name='buscarRelatorioMonitor'),
    path('buscarRelatorioTutor/<int:user_id>', views.buscarRelatorioTutor, name='buscarRelatorioTutor'),
    path('atualizarRelatorioMonitor/<int:relatorioM_id>', views.atualizarRelatorioMonitor, name='atualizarRelatorioMonitor'),
    path('atualizarRelatorioTutor/<int:relatorioT_id>', views.atualizarRelatorioTutor, name='atualizarRelatorioTutor'),
    path('deletarRelatorioMonitor/<int:relM_id>', views.deletarRelatorioMonitor, name='deletarRelatorioMonitor'),
    path('deletarRelatorioTutor/<int:relT_id>', views.deletarRelatorioTutor, name='deletarRelatorioTutor'),
]