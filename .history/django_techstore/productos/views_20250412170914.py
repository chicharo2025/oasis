from django.shortcuts import render
from .models import Producto, Categoria

def index(request):
    categoria = Categoria.objects.all()
    productos_oferta = Producto.objects.filter(en_oferta=True)
    productos = Producto.objects.all()
    return render(request, 'productos/index.html', {
        'categoria': categoria,
        'productos_oferta': productos_oferta,
        'productos': productos
    })

def detalle_producto(request, id_productos):
    producto = Producto.objects.get(id=id_productos)
    return render(request, 'productos/detalle.html', {'producto': producto})


def index(request):
    return render(request, 'productos/index.html')

def categorias(request):
    return render(request, 'productos/categoria.html')

def productos(request):
    return render(request, 'productos/catalogo.html')