from django.db import models

# Clase para mostrar la prediccion de la demanda y sus tendencias.
class PrediccionDemanda(models.Model):
    producto = models.CharField(max_length=100)
    prediccion_demanda = models.FloatField()
    fecha_prediccion = models.DateField()

# Clase para optimizar las rutas y minimizar costos.
class RutasOptimizadas(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    distancia = models.FloatField()
    ruta_optima = models.TextField()
    fecha_generacion = models.DateTimeField(auto_now_add=True)

# Clase para mantener un inventario limpio y actualizado 
class Inventario(models.Model):
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=20)
    fecha_actualizada = models.DateTimeField(auto_now=True)

# Clase para simular escenarios y realizar comparativas
class SimulacionEscenario(models.Model):
    nombre = models.CharField(max_length=100)
    costo_estimado = models.FloatField()
    tiempo_estimado = models.FloatField()
    fecha_simulacion = models.DateTimeField(auto_now_add=True)