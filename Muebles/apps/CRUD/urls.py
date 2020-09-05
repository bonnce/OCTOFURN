from django.urls import path
from . import views

app_name='CRUD'

urlpatterns = [
    path('mostrar',views.Mostrar,name="mostrar"),
    path('cargar',views.Cargar,name="cargar"),
    path('<pk>/borrar',views.Borrar,name="borrar"),
    path('<pk>/editar',views.Editar,name="editar"),
    path('buscar',views.Buscar,name="buscar"),
]