from django.urls import path
from .views import livro_list, livro_detail, livro_create, livro_update, livro_delete

urlpatterns = [
    path('', livro_list, name='livro_list'),
    path('livro/<int:pk>/', livro_detail, name='livro_detail'),
    path('livro/new/', livro_create, name='livro_create'),
    path('livro/<int:pk>/edit/', livro_update, name='livro_update'),
    path('livro/<int:pk>/delete/', livro_delete, name='livro_delete'),
]