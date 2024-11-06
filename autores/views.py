from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor
from .forms import AutorForm

def autor_list(request):
    autores = Autor.objects.all()
    return render(request, 'autores/autor_list.html', {'autores': autores})

def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm()
    return render(request, 'autores/autor_form.html', {'form': form})

def autor_update(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'autores/autor_form.html', {'form': form})

def autor_delete(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('autor_list')
    return render(request, 'autores/autor_confirm_delete.html', {'autor': autor})