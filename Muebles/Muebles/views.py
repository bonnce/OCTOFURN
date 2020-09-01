from django.shortcuts import render

def Home(request):
    return render(request,"home.html")

def MostrarP(request):
    return render(request,"mostrarProductos.html",{'Pestado':True})