from django.shortcuts import render
from . import models,forms
from ..CRUD import views
# Create your views here.

def Cr(request,btn):
    path='Pedidos:CR'
    path2='Pedidos:UD'
    if(btn=='mostrar'):
        return views.Mostrar(request,models.Pedidos,'Pedidos/CRUDPE.html',path,path2)
    elif(btn=='cargar'):
        return views.Cargar(request,models.Pedidos,forms.ClientForm,path,path2)
    elif(btn=='buscar'):
        return views.Buscar(request,models.Pedidos,path,path2)
    return None
def Ud(request,pk,btn):
    path='Pedidos:CR'
    path2='Pedidos:UD'
    if(btn=='editar'):
        return views.Editar(request,models.Pedidos,forms.ClientForm,pk,path,path2)
    elif(btn=='borrar'):
        return views.Borrar(request,models.Pedidos,pk,path,path2)
    return None
