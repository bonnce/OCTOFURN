from django.shortcuts import render
from . import models,forms
from ..CRUD import views

def Cr(request,btn):
    path='Herramientas:CR'
    path2='Herramientas:UD'
    if(btn=='mostrar'):
        return views.Mostrar(request,models.Herramientas,'Herramientas/CRUDH.html',path,path2)
    elif(btn=='cargar'):
        return views.Cargar(request,models.Herramientas,forms.ClientForm,path,path2)
    elif(btn=='buscar'):
        return views.Buscar(request,models.Herramientas,path,path2)
    return None
def Ud(request,pk,btn):
    path='Herramientas:CR'
    path2='Herramientas:UD'
    if(btn=='editar'):
        return views.Editar(request,models.Herramientas,forms.ClientForm,pk,path,path2)
    elif(btn=='borrar'):
        return views.Borrar(request,models.Herramientas,pk,path,path2)
    return None
