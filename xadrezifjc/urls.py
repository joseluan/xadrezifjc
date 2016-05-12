# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^entrar/','livros.views.entrar',name='entrar'),
    url(r'^sair/','livros.views.sair',name='sair'),
    url(r'^$','livros.views.index', name='livrosindex'),
    url(r'^livros/','livros.views.livros', name='livros'),
    url(r'^adicionar/','livros.views.adicionar', name='adicionar'),
    url(r'^emprestimo/','livros.views.emprestimo', name='emprestimo'),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': './media/'}),
    url(r'^blog/postagem/(?P<pk>[0-9]+)/$', 'postagens.views.postagem', name='postagem'),
    url(r'^blog/','postagens.views.index', name='blogindex'),
]
