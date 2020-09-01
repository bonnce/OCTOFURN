from django.urls import path
from . import views

app_name='Clientes'

urlpatterns = [
    path('mostrarC',views.MostrarC,name="mostrarC"),
    path('cargarC',views.CargarC,name="cargarC"),
    path('<pk>/borrarC',views.borrarC,name="borrarC"),
    path('<pk>/editarC',views.editarC,name="editarC"),
    path('<fname>/buscarC',views.buscarC,name="buscarC"),
]