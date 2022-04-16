import uuid
from django.db import models

class Disciplina (models.Model):
    nome = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome

class Curso (models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome

class Aluno (models.Model):
    nome_completo = models.CharField(max_length=60)
    matricula = models.CharField(max_length=12, unique=True)
    telefone = models.CharField(max_length=12)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    email = models.EmailField(verbose_name='e-mail')
    disciplinas = models.ManyToManyField(Disciplina)


    def __str__(self):
        return f'{self.matricula}'

class Professor (models.Model):
    nome_completo = models.CharField(max_length=60)
    matricula = models.CharField(max_length=12, unique=True)
    telefone = models.CharField(max_length=12)
    email = models.EmailField(verbose_name='e-mail')
    disciplinas = models.ForeignKey('Disciplina', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.matricula}'
    



