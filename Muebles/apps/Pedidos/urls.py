from django.urls import path
from . import views

app_name='Pedidos'

urlpatterns = [
    path('<btn>/CR',views.Cr,name="CR"),
    path('<int:pk>/<btn>/UD',views.Ud,name="UD"),
]