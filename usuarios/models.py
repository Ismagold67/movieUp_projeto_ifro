from django.db import models

# Create your models here.
class Filme(models.Model):
    usuario = models.CharField(max_length=50)
    situacao = models.CharField(max_length=10)
    titulo = models.CharField(max_length=100)
    sinopse = models.CharField(max_length=100)
    genero = models.CharField(max_length=20)
    data_lancamento = models.CharField(max_length=30)
    duracao = models.CharField(max_length=4)
    url_img = models.CharField(max_length=500, blank=True, null=True)
