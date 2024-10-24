from django.shortcuts import render
from blog.models import Categoria, Post

# Create your views here.

def Blog(request):
    posts = Post.objects.all()
    
    return render (request, "blog/Blog.html", {"posts": posts})

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(Categoria=categoria)
    return render(request, "blog/categorias.html", {"categoria": categoria, "posts": posts})

