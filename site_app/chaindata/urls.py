from django.urls import path
from chaindata.views import *

urlpatterns = [
    path('dashboard_prediccion/', dashboard_prediccion, name='dashboard_prediccion'),
]
