#-*- coding: utf-8 -*-
from models import *
from django.contrib import admin
from postagens.models import *
class ComentarioInline(admin.TabularInline):
	model = Comentario
	extra = 0

class ComentarioAdmin(admin.ModelAdmin):	
	list_display=['nome','seu_texto']
	save_on_top = True
	search_fields = ['post__title','nome']	

class PostarAdmin(admin.ModelAdmin):
	list_display=['title','data_publicacao']
	save_on_top = True
	search_fields = ['title']
	fieldsets = ((None, {'fields': ('title','foto','text','data_publicacao')}),)
	inlines = [ComentarioInline]

admin.site.register(Postar,PostarAdmin,)
admin.site.register(Comentario,ComentarioAdmin,)
