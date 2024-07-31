
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index_view, name='index'),  # URL pour la page d'accueil
    path('about/', views.about, name='about'),  # Route pour la page About
    path('projects/', views.projects, name='projects')  # Route pour la page Projects
]
