from django.shortcuts import render

def home(request):
    return render(request, 'tienda/index.html')

def detalle(request):
    return render(request, 'tienda/detalle.html')

def carrito(request):
    return render(request, 'tienda/carrito.html')

def contacto(request):
    return render(request, 'tienda/contacto.html')
