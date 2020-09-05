from django.shortcuts import render
from . import models,forms
from ..CRUD import views
# Create your views here.

def Cr(request,btn):
    path='Proveedores:CR'
    path2='Proveedores:UD'
    if(btn=='mostrar'):
        return views.Mostrar(request,models.Proveedores,'Proveedores/CRUDPV.html',path,path2)
    elif(btn=='cargar'):
        return views.Cargar(request,models.Proveedores,forms.ClientForm,path,path2)
    elif(btn=='buscar'):
        return views.Buscar(request,models.Proveedores,path,path2)
    return None
def Ud(request,pk,btn):
    path='Proveedores:CR'
    path2='Proveedores:UD'
    if(btn=='editar'):
        return views.Editar(request,models.Proveedores,forms.ClientForm,pk,path,path2)
    elif(btn=='borrar'):
        return views.Borrar(request,models.Proveedores,pk,path,path2)
    return None