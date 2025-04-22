from django.shortcuts import render, HttpResponse, redirect
from .models import Producto, Categoria,Carrito



def index(request):
    categorias = Categoria.objects.all()
    productos_oferta = Producto.objects.filter(en_oferta=True)
    productos = Producto.objects.filter(destacado=True)[:4]  # Limita a 4 productos
    return render(request, 'productos/index.html', {
        'categorias': categorias,
        'productos_oferta': productos_oferta,
        'productos': productos,
    })

def detalle_producto(request):
    producto = Producto.objects.filter().first()
    return render(request, 'productos/detalle.html', {'producto': producto})



def categorias(request):
    producto = Producto.objects.all()
    return render(request, 'productos/categoria.html', {'productos': producto,})


def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'productos/catalogo.html', {'productos': productos,})

def carrito(request):
    productos = Producto.objects.all()
    return render(request, 'productos/carrito.html', {'productos': productos,})

def añadir_al_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("carrito")


