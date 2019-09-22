from django.db import models

# Criando a classse Livro
class Livro(models.Model):

    class Meta:

# Criando a tabela livro
        db_table = 'livro'

# Criando os campos da tabela
    id = models.IntegerField(primary_key=True)
    titulo_livro = models.CharField(max_length=200)
    nome_autor = models.CharField(max_length=200)
    isbn = models.IntegerField(max_length=20)
    resumo = models.TextField(blank = True)

# Função que retornar os valores dos campos da tabela
    def __str__(self):
        return self.titulo_livro
        return self.nome_autor
        return self.isbn
        return self.resumo
