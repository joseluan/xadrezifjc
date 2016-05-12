from django.shortcuts import render, get_object_or_404
from postagens.models import *
from django.utils import timezone
from random import randint

def postagem(request, pk):

    post = get_object_or_404(Postar, pk=pk)
    title_postar = Postar.objects.get(id=pk).title
    text_postar = Postar.objects.get(id=pk).text
    total_comentarios = len(Comentario.objects.all().filter(post__title=title_postar))    

    if request.method == 'GET':
        return render(request, 'post.html', {
            'total_comentarios': total_comentarios,
        	'post': post,
        	'data': timezone.now().date,
        	})  
    else:

        Comentario.objects.create(post=Postar.objects.get(id=pk),nome=request.POST.get("nome"), seu_texto=request.POST.get("textoarea")).save()		
        return render(request, 'post.html', {
            'total_comentarios': total_comentarios,
        	'post': post,
        	'data': timezone.now().date,
        	})  
     

def index(request):

    p = Postar.objects.all()[::-1]
    #contador = 0
    #for post in p:
    #    p[contador].foto.name = post.foto.name[17:-1]+'g'
    #    contador += 1
    return render(request,'indexblog.html',{
        'titulo': randint(0,len(Comentario.objects.all() ) ),
        'texto': len(Comentario.objects.all()),
		'data': timezone.now().date,
		'posts': p
		
        })
