from rest_framework import serializers
from .models import Livro

# Criando a classe Serializer(json)
class LivrosSerializer(serializers.ModelSerializer):

    class Meta:

        model = Livro
# Todos os campos seram serializados
        fields = '__all__'
