from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.


#def Autenticacion(request):
    #return render(request,"registro/Registro.html")

class VRegistro(View):
    def get(self, request):
        form=UserCreationForm()
        return render(request, 'registro/Registro.html', {"form":form})

    def post(self, request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

        return render(request, 'registro/Registro.html', {"form":form})
    

def cerrar_cesion(request):
    logout(request)
    return redirect('home')


def logear(request):
    if request.method=="POST":
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, "Usuario no valido")
        else:
            messages.error(request, "Datos invalidos, por favor revise que el usuario y la contraseña sean correctos")

    form = AuthenticationForm
    return render (request, 'login/Login.html', {"form":form})