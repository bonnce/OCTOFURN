from django.shortcuts import render
from . import models,forms
from ..CRUD import views
# Create your views here.

def Cr(request,btn):
    path='Productos:CR'
    path2='Productos:UD'
    if(btn=='mostrar'):
        return views.Mostrar(request,models.Productos,'Productos/CRUDPR.html',path,path2)
    elif(btn=='cargar'):
        return views.Cargar(request,models.Productos,forms.ClientForm,path,path2)
    elif(btn=='buscar'):
        return views.Buscar(request,models.Productos,path,path2)
    return None
def Ud(request,pk,btn):
    path='Productos:CR'
    path2='Productos:UD'
    if(btn=='editar'):
        return views.Editar(request,models.Productos,forms.ClientForm,pk,path,path2)
    elif(btn=='borrar'):
        return views.Borrar(request,models.Productos,pk,path,path2)
    return None
