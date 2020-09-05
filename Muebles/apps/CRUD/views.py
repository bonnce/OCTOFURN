from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse,request
# Create your views here.

def Mostrar(request,model,template,path,path2):
    objetos=model.objects.all()
    return render(request,template,{'objetos':objetos,'estado':True,'path':path,'path2':path2})

def Guardar_form(request,model,form,template_name,path,path2):
    data={}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            objetos=model.objects.all()
            data['html_lista']=render_to_string('CRUD/list.html',{'objetos':objetos,'path':path,'path2':path2})
        else:
            data['form_is_valid'] = False
            
    context = {'form': form,'path':path,'path2':path2}
    data['html_form']=render_to_string(template_name,context,request)
    return JsonResponse(data)

def Cargar(request,model,form,path,path2):
    if request.method == 'POST':
        f = form(request.POST)
    else:
        f=form()
    return Guardar_form(request,model,f,'CRUD/create_form.html',path,path2)

def Editar(request,model,form,pk,path,path2):
    objeto=get_object_or_404(model,pk=pk)
    if request.method == 'POST':
        f = form(request.POST,instance=objeto)
    else:
        f=form(instance=objeto)
    return Guardar_form(request,model,f,'CRUD/update_form.html',path,path2)

def Buscar(request,model,path,path2):
    data={}
    b=request.GET.get('b',None)
    if(request.method=='GET'):
        if(b==""):
            objetos=model.objects.all()
        else:
            objetos=get_list_or_404(model,first_name__icontains=b)
        data['html_lista']=render_to_string('CRUD/list.html',{'objetos':objetos,'path':path,'path2':path2},request)
    else:
        objetos=model.objects.all()
    print("esto es data",data)
    return JsonResponse(data)

def Borrar(request,model,pk,path,path2):
    data={}
    objeto=get_object_or_404(model,pk=pk)
    if request.method == 'POST':
        objeto.delete()
        data['form_is_valid'] = True
        objetos=model.objects.all()
        data['html_lista']=render_to_string('CRUD/list.html',{'objetos':objetos,'path':path,'path2':path2})
    else:
        context={'objeto':objeto,'path':path,'path2':path2}
        data['html_form']=render_to_string('CRUD/delete_form.html',context,request)
    return JsonResponse(data)