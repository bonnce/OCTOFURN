from django.shortcuts import render
from . import models,forms
from ..CRUD import views
# Create your views here.

def Cr(request,btn):
    path='Insumos:CR'
    path2='Insumos:UD'
    if(btn=='mostrar'):
        return views.Mostrar(request,models.Insumos,'Insumos/CRUDI.html',path,path2)
    elif(btn=='cargar'):
        return views.Cargar(request,models.Insumos,forms.ClientForm,path,path2)
    elif(btn=='buscar'):
        return views.Buscar(request,models.Insumos,path,path2)
    return None
def Ud(request,pk,btn):
    path='Insumos:CR'
    path2='Insumos:UD'
    if(btn=='editar'):
        return views.Editar(request,models.Insumos,forms.ClientForm,pk,path,path2)
    elif(btn=='borrar'):
        return views.Borrar(request,models.Insumos,pk,path,path2)
    return None