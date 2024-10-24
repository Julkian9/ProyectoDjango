from django.shortcuts import render
from .models import Producto, CategoriaProd

# Create your views here.


def Tienda(request):
    producto = Producto.objects.all()
    return render (request, "tienda/Tienda.html", {"productos":producto})

def Filtro(request, categoria_id):
    categoria = CategoriaProd.objects.get(id=categoria_id)
    producto = Producto.objects.filter(Categoria=categoria)
    return render(request, "tienda/Tienda.html", {"categoria": categoria, "producto":producto})