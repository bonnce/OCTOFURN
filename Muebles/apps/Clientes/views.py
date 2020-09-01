from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
from . import models,forms
# Create your views here.

def MostrarC(request):
    C=models.Clientes.objects.all()
    return render(request,'Clientes/mostrarClientes.html',{'client':C,'Cestado':True})

def guardar_form(request,form,template_name):
    data={}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            C=models.Clientes.objects.all()
            data['html_lista_cliente']=render_to_string('Clientes/listaCliente.html',{'client':C})
        else:
            data['form_is_valid'] = False
            
    context = {'form': form}
    data['html_form']=render_to_string(template_name,context,request)
    return JsonResponse(data)

def CargarC(request):
    if request.method == 'POST':
        form = forms.ClientForm(request.POST)
    else:
        form=forms.ClientForm()
    return guardar_form(request,form,'Clientes/cargarClientes.html')

def editarC(request,pk):
    client=get_object_or_404(models.Clientes,pk=pk)
    if request.method == 'POST':
        form = forms.ClientForm(request.POST,instance=client)
    else:
        form=forms.ClientForm(instance=client)
    return guardar_form(request,form,'Clientes/modificarClientes.html')

def buscarC(request,fname):
    data={}
    if(fname=="~"):
        client=models.Clientes.objects.all()
    else:
        client=get_list_or_404(models.Clientes,first_name__icontains=fname)
    data['html_lista_cliente']=render_to_string('Clientes/listaCliente.html',{'client':client},request)
    return JsonResponse(data)

def borrarC(request,pk):
    data={}
    client=get_object_or_404(models.Clientes,pk=pk)
    if request.method == 'POST':
        client.delete()
        data['form_is_valid'] = True
        C=models.Clientes.objects.all()
        data['html_lista_cliente']=render_to_string('Clientes/listaCliente.html',{'client':C})
    else:
        context={'client':client}
        data['html_form']=render_to_string('Clientes/borrarClientes.html',context,request)
    return JsonResponse(data)