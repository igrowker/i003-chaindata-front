from django.urls import path
from chaindata.views import inicio, register, login_user, prediccion_demanda, rutas_optimizadas, inventario, simulacion

urlpatterns = [
    path('', inicio, name='inicio'),
    path('registro/', register, name='registro'),
    path('login/', login_user, name='login'),
    path('prediccion/', prediccion_demanda, name='demanda'),
    path('rutas/', rutas_optimizadas, name='rutas'),
    path('inventario/', inventario, name='inventario'),
    path('simulacion/', simulacion, name='simulacion'),
]
