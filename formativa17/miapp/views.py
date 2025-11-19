from django.shortcuts import render, redirect
from .models import Autor, Libro
from .forms import AutorForm, LibroForm

def home(request):
    return render(request, 'home.html')

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'lista_autores.html', {'autores': autores})

def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'agregar_autor.html', {'form': form})

def lista_libros(request):
    libros = Libro.objects.all().select_related('autor')
    return render(request, 'lista_libros.html', {'libros': libros})

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'agregar_libro.html', {'form': form})