# from django.db import models

# class Autor(models.Model):
#     nome = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nome

# class Categoria(models.Model):
#     nome = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nome

# class Livro(models.Model):
#     nome = models.CharField(max_length=200)
#     quantidade_paginas = models.IntegerField()
#     categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
#     autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
#     isbn = models.CharField(max_length=13, unique=True)

#     def __str__(self):
#         return self.nome

from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    # Outros campos do autor

    def __str__(self):
        return self.nome

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)  # Chave estrangeira para Autor
    categoria = models.CharField(max_length=100)
    quantidade_paginas = models.IntegerField()
    isbn = models.CharField(max_length=20)

    def __str__(self):
        return self.nome