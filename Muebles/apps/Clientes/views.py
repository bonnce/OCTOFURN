from . import models,forms
from ..CRUD import views
# Create your views here.

def Cr(request,btn):
    path='Clientes:CR'
    path2='Clientes:UD'
    if(btn=='mostrar'):
        return views.Mostrar(request,models.Clientes,'Clientes/CRUDC.html',path,path2)
    elif(btn=='cargar'):
        return views.Cargar(request,models.Clientes,forms.ClientForm,path,path2)
    elif(btn=='buscar'):
        return views.Buscar(request,models.Clientes,path,path2)
    return None
def Ud(request,pk,btn):
    path='Clientes:CR'
    path2='Clientes:UD'
    if(btn=='editar'):
        return views.Editar(request,models.Clientes,forms.ClientForm,pk,path,path2)
    elif(btn=='borrar'):
        return views.Borrar(request,models.Clientes,pk,path,path2)
    return None