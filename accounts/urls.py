from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cadastro/', views.cadastro, name='cadastro'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastroAluno/', views.cadastroAluno, name='cadastroAluno'),
    path('cadastroMonitor', views.cadastroMonitor, name='cadastroMonitor'),
    path('cadastroTutor', views.cadastroTutor, name='cadastroTutor'),
    path('dashboardAluno/', views.dashboardAluno, name='dashboardAluno'),

    #template_name="accounts/reset_password.html"
    #template_name="accounts/password_reset_done.html"
    #template_name="accounts/password_reset_confirm.html"
    #template_name="accounts/password_reset_complete.html"

    # path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/reset_password.html"), name="reset_password"),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/reset_password_sent.html"), name="password_reset_done"),
    # path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name="password_reset_confirm"),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name="password_reset_complete"),

]