from django.urls import path
from .views import autor_list, autor_create, autor_update, autor_delete

urlpatterns = [
    path('', autor_list, name='autor_list'),
    path('novo/', autor_create, name='autor_create'),
    path('editar/<int:pk>/', autor_update, name='autor_update'),
    path('deletar/<int:pk>/', autor_delete, name='autor_delete'),
]