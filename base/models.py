from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Curso(models.Model):
    nome = models.CharField(max_length=40)
    horario = models.CharField(max_length=60)
    duracao = models.IntegerField()
    localidade = models.CharField(max_length=60)
    localizacao = models.CharField(max_length=60)
    accao = models.CharField(max_length=20)


    def __str__(self) -> str:
        return self.nome

class Formador(models.Model):
    nome = models.CharField(max_length=40)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)


    def __str__(self) -> str:
        return self.nome


class Formando(models.Model):
    nome = models.CharField(max_length=60)
    habilitacoes = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    contacto = models.IntegerField()
    morada = models.CharField(max_length=60)
    codigo_postal = models.CharField(max_length=20)
    localidade = models.CharField(max_length=20)
    bi = models.CharField(max_length=20)
    validade = models.CharField(max_length=20)
    data_nascimento = models.CharField(max_length=20)
    natural = models.CharField(max_length=20)
    nacionalidade = models.CharField(max_length=20)
    nif = models.CharField(max_length=20)
    observacoes = models.TextField()
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    formador = models.ForeignKey(Formador, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome



