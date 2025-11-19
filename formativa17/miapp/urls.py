from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('autores/', views.lista_autores, name='lista_autores'),
    path('agregar-autor/', views.agregar_autor, name='agregar_autor'),
    path('libros/', views.lista_libros, name='lista_libros'),
    path('agregar-libro/', views.agregar_libro, name='agregar_libro'),
]