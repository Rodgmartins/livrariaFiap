# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Livro
# from .forms import LivroForm  # Vamos criar esse formulário em breve

# def livro_list(request):
#     livros = Livro.objects.all()
#     return render(request, 'livros/livro_list.html', {'livros': livros})

# def livro_detail(request, pk):
#     livro = get_object_or_404(Livro, pk=pk)
#     return render(request, 'livros/livro_detail.html', {'livro': livro})

# def livro_create(request):
#     if request.method == "POST":
#         form = LivroForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('livro_list')
#     else:
#         form = LivroForm()
#     return render(request, 'livros/livro_form.html', {'form': form})

# def livro_update(request, pk):
#     livro = get_object_or_404(Livro, pk=pk)
#     if request.method == "POST":
#         form = LivroForm(request.POST, instance=livro)
#         if form.is_valid():
#             form.save()
#             return redirect('livro_list')
#     else:
#         form = LivroForm(instance=livro)
#     return render(request, 'livros/livro_form.html', {'form': form})

# def livro_delete(request, pk):
#     livro = get_object_or_404(Livro, pk=pk)
#     if request.method == "POST":
#         livro.delete()
#         return redirect('livro_list')
#     return render(request, 'livros/livro_confirm_delete.html', {'livro': livro})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro
from .forms import LivroForm

def livro_list(request):
    livros = Livro.objects.all()
    return render(request, 'livros/livro_list.html', {'livros': livros})

def livro_detail(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'livros/livro_detail.html', {'livro': livro})

def livro_create(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livro_list')
    else:
        form = LivroForm()
    return render(request, 'livros/livro_form.html', {'form': form})

def livro_update(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == "POST":
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livro_detail', pk=livro.pk)
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livros/livro_form.html', {'form': form})

def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == "POST":
        livro.delete()
        return redirect('livro_list')
    return render(request, 'livros/livro_confirm_delete.html', {'livro': livro})