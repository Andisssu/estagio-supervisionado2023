from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.feeIndex, name='feeIndex'),
    path('adicionarFeedback', views.adicionarFeedback, name='adicionarFeedback'),
    path('buscarFeedback', views.buscarFeedback, name='buscarFeedback'),
    path('feedback/<int:feedback_id>', views.feedback, name='feedback'),
    path('atualizarFeedback/<int:feedback_id>', views.atualizarFeedback, name='atualizarFeedback'),

    path('feedback/baixarFileFeedback/<str:filename>/', views.baixarFileFeedback, name='baixarFileFeedback'),

    #ADMIN
    path('feedback/adminFeedbackAll', views.adminFeedbackAll, name='adminFeedbackAll'),
    path('feedback/adminFeedbackAll/adminOpenfeedback/<int:feedback_id>', views.adminOpenfeedback, name='adminOpenfeedback'),
    path('feedback/adminFeedbackAll/adminOpenAllfeedback/<int:feedback_id>', views.adminOpenAllfeedback, name='adminOpenAllfeedback'),
    path('feedback/adminRespostaFeedback/<int:feedback_id>/', views.adminRespostaFeedback, name='adminRespostaFeedback'),
    path('feedback/adminDeletarFeedback/<int:feedback_id>/', views.adminDeletarFeedback, name='adminDeletarFeedback'),
    path('feedback/adminMarcarComoLido/<int:feedback_id>/', views.adminMarcarComoLido, name='adminMarcarComoLido'),

    #ALUNO
    path('feedback/alunoFeedback/<int:user_id>', views.alunoFeedback, name='alunoFeedback'),
    path('feedback/alunoFeedbackAll/<int:user_id>', views.alunoFeedbackAll, name='alunoFeedbackAll'),
    path('feedback/alunoFeedbackAll/<int:user_id>/alunoOpenfeedback/<int:feedback_id>', views.alunoOpenfeedback, name='alunoOpenfeedback'),
    path('feedback/alunoFeedbackAll/<int:user_id>/alunoOpenAllfeedback/<int:feedback_id>', views.alunoOpenAllfeedback, name='alunoOpenAllfeedback'),
    path('feedback/alunoRespostaFeedback/<int:user_id>/<int:feedback_id>/', views.alunoRespostaFeedback, name='alunoRespostaFeedback'),
    path('feedback/alunoMarcarComoLido/<int:feedback_id>/', views.alunoMarcarComoLido, name='alunoMarcarComoLido'),

    #MONITOR
    path('feedback/monitorFeedback/<int:user_id>', views.monitorFeedback, name='monitorFeedback'),
    path('feedback/monitorFeedbackAll/<int:user_id>', views.monitorFeedbackAll, name='monitorFeedbackAll'),
    path('feedback/monitorFeedbackAll/<int:user_id>/monitorOpenfeedback/<int:feedback_id>', views.monitorOpenfeedback, name='monitorOpenfeedback'),
    path('feedback/monitorFeedbackAll/<int:user_id>/monitorOpenAllfeedback/<int:feedback_id>', views.monitorOpenAllfeedback, name='monitorOpenAllfeedback'),
    path('feedback/monitorRespostaFeedback/<int:user_id>/<int:feedback_id>/', views.monitorRespostaFeedback, name='monitorRespostaFeedback'),
    path('feedback/monitorMarcarComoLido/<int:feedback_id>/', views.monitorMarcarComoLido, name='monitorMarcarComoLido'),

    #TUTOR
    path('feedback/tutorFeedback/<int:user_id>', views.tutorFeedback, name='tutorFeedback'),
    path('feedback/tutorFeedbackAll/<int:user_id>', views.tutorFeedbackAll, name='tutorFeedbackAll'),
    path('feedback/tutorFeedbackAll/<int:user_id>/tutorOpenfeedback/<int:feedback_id>', views.tutorOpenfeedback, name='tutorOpenfeedback'),
    path('feedback/tutorFeedbackAll/<int:user_id>/tutorOpenAllfeedback/<int:feedback_id>', views.tutorOpenAllfeedback, name='tutorOpenAllfeedback'),
    path('feedback/tutorRespostaFeedback/<int:user_id>/<int:feedback_id>/', views.tutorRespostaFeedback, name='tutorRespostaFeedback'),
    path('feedback/tutorMarcarComoLido/<int:feedback_id>/', views.tutorMarcarComoLido, name='tutorMarcarComoLido'),

]