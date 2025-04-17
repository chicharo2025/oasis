from django.shortcuts import render
from .models import Producto, Categoria

def index(request):
    categorias = Categoria.objects.all()
    productos_oferta = Producto.objects.filter(en_oferta=True)
    productos = Producto.objects.all()
    return render(request, 'productos/index.html', {
        'categorias': categorias,
        'productos_oferta': productos_oferta,
        'productos': productos
    })

def detalle_producto(request, id_productos):
    producto = Producto.objects.get(id=id_productos)
    return render(request, 'productos/detalle.html', {'producto': producto})


def index(request):
    return render(request, 'productos/index.html')

def categorias(request):
    return render(request, 'productos/categorias.html')

def productos(request):
    return render(request, 'productos/productos.html')