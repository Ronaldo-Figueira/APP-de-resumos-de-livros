from django.conf.urls import url
from . import views
from django.urls import path, include

# Adicionando a ulr para a acessar a view LivrosLista da classe genérica
urlpatterns = [
    url('livros/', views.LivrosLista.as_view(), name='LivrosLista'),

]
