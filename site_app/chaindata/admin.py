from django.contrib import admin
from .models import Inventario, RutasOptimizadas, SimulacionEscenario, PrediccionDemanda

class InventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad')
    list_per_page = 15
    list_filter = ('producto',)

class RutasOptimizadasAdmin(admin.ModelAdmin):
    list_display = ('origen', 'destino')

admin.site.register(Inventario, InventarioAdmin)
admin.site.register(RutasOptimizadas, RutasOptimizadasAdmin)
admin.site.register(SimulacionEscenario)
admin.site.register(PrediccionDemanda)
