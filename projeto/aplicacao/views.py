from django.shortcuts import render
from aplicacao.models import *
from django.http import HttpResponse

def evento(request):
	evento = Evento.objects.all()
	html = ""
	for e in evento:
		html += '<li>{} {}</li>'.format(e.nome, e.titulo)
	return HttpResponse(html)