from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('' , views.home , name='home'),
    path('all/utilisateur', views.lister , name='liste'),
    path('create', views.create , name='create'),
    path('modifier/<int:id>', views.modifier, name='modifier'),
    path('enregistrement/', views.enregistrer , name='enregistrer'),
    path('supprimer', views.supprimer, name='sup'),
]