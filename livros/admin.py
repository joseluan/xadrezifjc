# -*- coding: utf-8 -*-
from django.contrib import admin
from livros.models import *
# Register your models here.
admin.site.register(Livro)
admin.site.register(EmprestimoLivro)