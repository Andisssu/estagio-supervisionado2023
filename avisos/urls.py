from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('baixarFileAviso/<str:filename>', views.baixarFileAviso, name='baixarFileAviso'),

#ADMIN
    path('aviIndex', views.aviIndex, name='aviIndex'),
    path('adicionarAviso', views.adicionarAviso, name='adicionarAviso'),
    path('buscarAviso', views.buscarAviso, name='buscarAviso'),
    path('aviso/<int:aviso_id>', views.aviso, name='aviso'),
    path('atualizarAviso/<int:aviso_id>', views.atualizarAviso, name='atualizarAviso'),
    path('deletarAviso/<int:aviso_id>', views.deletarAviso, name='deletarAviso'),

#ALUNO
    path('aviIndexAluno', views.aviIndexAluno, name='aviIndexAluno'),
    path('buscarAvisoAluno', views.buscarAvisoAluno, name='buscarAvisoAluno'),
    path('avisoAluno/<int:aviso_id>', views.avisoAluno, name='avisoAluno'),

#MONITOR
    path('aviIndexMonitor', views.aviIndexMonitor, name='aviIndexMonitor'),
    path('buscarAvisoMonitor', views.buscarAvisoMonitor, name='buscarAvisoMonitor'),
    path('avisoMonitor/<int:aviso_id>', views.avisoMonitor, name='avisoMonitor'),

#TUTOR
    path('aviIndexTutor', views.aviIndexTutor, name='aviIndexTutor'),
    path('buscarAvisoTutor', views.buscarAvisoTutor, name='buscarAvisoTutor'),
    path('avisoTutor/<int:aviso_id>', views.avisoTutor, name='avisoTutor'),

#INTERPRETE
    path('aviIndexInterprete', views.aviIndexInterprete, name='aviIndexInterprete'),
    path('buscarAvisoInterprete', views.buscarAvisoInterprete, name='buscarAvisoInterprete'),
    path('avisoInterprete/<int:aviso_id>', views.avisoInterprete, name='avisoInterprete'),

]