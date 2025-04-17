from django.shortcuts import render
from .models import Producto, Categoria

def index(request):
    categorias = Categoria.objects.all()
    productos_oferta = Producto.objects.filter(en_oferta=True)
    producto = Producto.objects.all()
    return render(request, 'productos/index.html', {
        'categorias': categorias,
        'productos_oferta': productos_oferta,
        'producto': producto
    })

def detalle_producto(request, id_productos):
    producto = Producto.objects.get(id=id_productos)
    return render(request, 'productos/detalle.html', {'producto': producto})

def categoria(request):  # Nombre en singular para coincidir con urls.py
    categorias = Categoria.objects.all()
    return render(request, 'productos/categoria.html', {'categorias': categorias})


def catalogo(request):  # Función añadida
    productos = Producto.objects.all()
    return render(request, 'productos/producto.html', {'producto': productos})