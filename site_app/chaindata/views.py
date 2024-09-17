from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Inventario


# Vista del inicio
def inicio(request):
    return render(request, 'chaindata/inicio.html')

# Vista de prediccion de demanda
def prediccion_demanda(request):
    return render(request, 'chaindata/prediccion.html')

# Vista de rutas optimizadas
def rutas_optimizadas(request):
    return render(request, 'chaindata/rutas.html')

# Vista del inventario
def inventario(request):

    productos = Inventario.objects.all()
    contexto = {'productos': productos}
    return render(request, 'chaindata/inventario.html', contexto)

# Vista de simulacion de escenarios
def simulacion(request):
    return render(request, 'chaindata/simulacion.html')

# Vista para el registro de usuarios
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'chaindata/base.html')
        else:
            form = UserCreationForm(request.POST)
    else:
        form = UserCreationForm()
    return render(request, 'chaindata/register.html', {'form': form})

# Vista para el login de usuarios
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('chaindata:base')
        else:
            messages.error(request, 'Usuario o contraseña no validos')

    return render(request, 'chaindata/login.html')
