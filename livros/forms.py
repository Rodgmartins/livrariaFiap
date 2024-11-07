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
from .models import Livro, Autor

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'autor', 'categoria', 'quantidade_paginas', 'isbn']
        widgets = {
            'autor': forms.Select(attrs={'class': 'form-control'}),
        }