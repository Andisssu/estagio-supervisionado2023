from django.contrib import admin
from django.template.defaulttags import url

from django.urls import path, include
from . import views
urlpatterns = [
    path('ola', views.ola, name='ola')
]