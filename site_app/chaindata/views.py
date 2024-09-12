from django.shortcuts import render

def dashboard_prediccion(request):
    return render(request, 'chaindata/dashboard_prediccion.html')
