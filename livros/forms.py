# -- Tentativa 1
# from django import forms
# from .models import Livro

# class LivroForm(forms.ModelForm):
#     class Meta:
#         model = Livro
#         fields = ['nome', 'quantidade_paginas', 'categoria', 'autor', 'isbn']


# -- Tentativa 1
# from django import forms
# from .models import Livro, Autor

# class LivroForm(forms.ModelForm):
#     class Meta:
#         model = Livro
#         fields = ['nome', 'autor', 'categoria', 'quantidade_paginas', 'isbn']


# -- Tentativa 3
from django import forms
from .models import Livro
from autores.models import Autor
from django.forms.models import ModelChoiceField

class LivroForm(forms.ModelForm):
    autor = ModelChoiceField(queryset=Autor.objects.all())
    class Meta:
        model = Livro
        fields = ['nome', 'autor', 'categoria', 'quantidade_paginas', 'isbn']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['autor'] = ModelChoiceField(queryset=Autor.objects.all())

# autor = ModelChoiceField(queryset=Livro.objects.all())