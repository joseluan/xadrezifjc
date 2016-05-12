# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Livro(models.Model):

	class Meta:
		verbose_name_plural = 'Livros'
		verbose_name = 'Livro'

	titulo = models.CharField(verbose_name = 'Título', max_length = 40)
	autor = models.CharField(verbose_name = 'Autor', max_length = 20)
	numero = models.DecimalField(verbose_name = 'Número do livro', max_digits = 15, decimal_places = 0, default=0) 
	foto = models.ImageField(upload_to='livro/', height_field=None, width_field=None, max_length=100,blank=True,null=True,default='livro/default.jpg')

	def __str__(self):
		return self.titulo

class EmprestimoLivro(models.Model):

	from datetime import date

	livro = models.ForeignKey(Livro)
	nome = models.CharField(verbose_name = 'Nome', max_length = 40,default='nomeAluno')
	escola = models.CharField(verbose_name = 'Escola', max_length = 40,default='IFRN-JC')
	matricula = models.DecimalField(verbose_name = 'Matricula', max_digits = 20, decimal_places = 0, default=0) 

	if (date.today().day+15>31):
		novadata = data2-15
		data2 = novadata
	else:
		data2 = date.today().day+15
		
	datadevolucao = data2
	
	def __unicode__(self):
		return self.livro.titulo
		
	

