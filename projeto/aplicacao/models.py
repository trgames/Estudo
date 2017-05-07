from django.db import models

# Create your models here.

class Evento(models.Model):
	nome = models.CharField('nome', max_length=200)
	sigla = models.CharField('sigla', max_length=200)
	titulo = models.CharField('titulo', max_length=200)
	dataInicio = models.DateTimeField('data de inicio')
	realizador = models.ForeignKey('Pessoa')

class Pessoa(models.Model):
	nome = models.CharField('nome', max_length=200)
	cpf = models.CharField('cpf', max_length=15)