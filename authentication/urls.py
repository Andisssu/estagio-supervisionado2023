from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('authLogin', views.authLogin, name='authLogin'),
    path('authLogout', views.authLogout, name='authLogout'),
    path('authRegister', views.authRegister, name='authRegister'),
    path('authRegisterGeral', views.authRegisterGeral, name='authRegisterGeral'),
    path('authRegisterAluno', views.authRegisterAluno, name='authRegisterAluno'),
    path('authRegisterMonitor', views.authRegisterMonitor, name='authRegisterMonitor'),
    path('authRegisterTutor', views.authRegisterTutor, name='authRegisterTutor'),
    path('authRegisterInterprete', views.authRegisterInterprete, name='authRegisterInterprete'),

    #Recuperação de senha
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="authenticate/password_reset.html"), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="authenticate/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="authenticate/password_reset_confirm.html"), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="authenticate/password_reset_complete.html"), name="password_reset_complete"),
]