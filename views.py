from rest_framework import generics
from .models import Livro
from .serializers import LivrosSerializer

# Criando a classe genérica que possui os métodos GET, POST
class LivrosLista(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivrosSerializer
