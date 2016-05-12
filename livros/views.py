# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, logout, login

from livros.forms import *
from livros.models import *

def entrar(request):
	if request.method=='POST':
		cusuario = request.POST.get("usuario")
		csenha = request.POST.get("senha")

		user = authenticate(username=cusuario, password=csenha)
		if user is not None:
			if user.is_active:
				login(request, user)
				request.session['usuario'] = cusuario
				return HttpResponseRedirect('/') 
			else:
				return render(request, 'entrar.html',{
					'usuario': user
					}) 
		else:
			
			return render(request, 'entrar.html',{
				'usuario': user,
					})  

	return render(request,'entrar.html',{
		'usuario': True,
		})
def index(request):

	return render(request,'index.html',{
		'livros': Livro.objects.all(),
		})

def sair(request):
	logout(request)
	request.session.flush()
	return HttpResponseRedirect('/')	

@login_required(login_url='/entrar/')
def livros(request):
	if request.method == "POST":
		titulo=request.POST.get("titulo")

		return render(request,'livros.html',{
		'livros': Livro.objects.filter(titulo__contains=titulo+""),
		})
	else:

		return render(request,'livros.html',{
		'livros': Livro.objects.all(),
		})

@login_required(login_url='/entrar/')
def adicionar(request):
	form = FormFotoCliente()  
	if request.method == "POST":
		form = FormFotoCliente(request.POST, request.FILES)
		lv = Livro.objects.create(titulo=request.POST.get("titulo"), autor=request.POST.get("autor"), numero=request.POST.get("numero"))
		lv.save()
		return render(request,'adicionar.html',{
			'form': form,
			'lv': request.FILES.keys(),})
	else:
		return render(request,'adicionar.html',{'form': form,})

@login_required(login_url='/entrar/')
def emprestimo(request):
	if request.method == "POST":
		livronome=request.POST.get('livro')
		EmprestimoLivro.objects.create(livro= Livro.objects.get(titulo=livronome),nome=request.POST.get("nome"),escola=request.POST.get("escola")).save()

		return render(request,'emprestimo.html',{
		})
	else:

		return render(request,'emprestimo.html',{
		'livros': Livro.objects.all(),
		})