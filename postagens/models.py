# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Postar(models.Model):

    title = models.CharField(max_length=200)
    foto = models.ImageField(max_length=255, blank=True, upload_to='imagens_noticias/', verbose_name='Foto')
    text = models.TextField()
    data_publicacao = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    class Meta:
		verbose_name_plural = 'Postagens'
		verbose_name = 'Postagem'

    def __str__(self):
        return self.title

class Comentario(models.Model):
    post = models.ForeignKey(Postar)
    nome = models.CharField(max_length=50)
    seu_texto = models.TextField()
    class Meta:
		verbose_name_plural = 'Comentarios'
		verbose_name = 'Comentario'

    def __str__(self):
        return self.nome