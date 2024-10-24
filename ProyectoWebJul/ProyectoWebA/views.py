from django.shortcuts import render, HttpResponse
from carro.carro import Carro


# Create your views here.

def Home(request):
    carro=Carro(request)
    return render (request, "ProyectoWebA/Home.html")





