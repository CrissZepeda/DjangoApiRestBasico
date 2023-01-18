from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages
from .models import Reservas
from .forms import registerReserva
from .serializers import ReservasSerializer
#from api.views import ReservaViewset
from django.urls import reverse
import requests

from django.forms.models import model_to_dict

# Create your views here.

def login_user(request):
    if request.user.id:
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        if request.method == "POST":
            username = request.POST["username"]
            contrasena = request.POST["password"]
            user = authenticate(request, username=username, password=contrasena)
            if user is not None:
                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                messages.error(request, "¡Usuario o contraseña incorrectos!")
                return redirect(settings.LOGIN_URL)
        else:
            form = AuthenticationForm()
            return render(request, "login.html", {'form': form})

def registrarse(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

@login_required
def logout_user(request):
    logout(request)
    return redirect(settings.LOGIN_URL)

@login_required
def inicio(request):
    return render(request, "inicio.html")

@login_required
def reservas(request):
    if request.method == 'POST':
        form = registerReserva(request.POST)
        if form.is_valid():
            #print(ReservasSerializer(request.POST))
            
            nombre = request.POST['nombre']
            fono = request.POST['fono']
            fecha = request.POST['fecha']
            hora = request.POST['hora']
            cantidad = request.POST['cantidad']
            observacion = request.POST['observacion']
            
            url = 'http://localhost:8000/api/reserva/'
            params = {"nombre":nombre,"fono":fono,"fecha":fecha,"hora":hora,"cantidad":cantidad,"observacion":observacion}
            headers = {'Content-Type': 'application/json'}

            response = requests.post(url, json=params, headers=headers)
            
            #print(response.json())
            datos = response.json()
            #form.save()        
            return redirect("/lista")
        
    else:
        form = registerReserva()
        
    return render(request, "reservas.html", {"form": form})

@login_required
def listReserva(request):
    url = 'http://localhost:8000/api/reserva/'

    response = requests.get(url)
    data = response.json()
    return render(request, "lista_reserva.html", {"data": data})

@login_required
def eliminarReserva(request,id):
    url = 'http://localhost:8000/api/reserva/'+str(id)    
    response = requests.delete(url)
    return redirect("lista")

def actualizaReserva(request,id):
    url = 'http://localhost:8000/api/reserva/'+str(id)+'/'
    print(url) 
    response = requests.get(url)
    print(response.json())
    
    if request.method == "POST":
        form = registerReserva(request.POST, response.json())
        if form.is_valid():
            
            nombre = request.POST['nombre']
            fono = request.POST['fono']
            fecha = request.POST['fecha']
            hora = request.POST['hora']
            cantidad = request.POST['cantidad']
            observacion = request.POST['observacion']
            
            url = 'http://localhost:8000/api/reserva/'+str(id)+'/'
            params = {"nombre":nombre,"fono":fono,"fecha":fecha,"hora":hora,"cantidad":cantidad,"observacion":observacion}
            headers = {'Content-Type': 'application/json'}

            response = requests.put(url, json=params, headers=headers)
            
            return redirect("/lista")
        
    form = registerReserva(response.json())
    return render(request, "reservas.html", {"form": form})
