from django.shortcuts import render, get_object_or_404 , redirect
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


def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
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

from django.shortcuts import get_object_or_404, redirect
from productos.models import Producto

def añadir_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    carrito = request.session.get('carrito', {})

    producto_id_str = str(producto.id)

    if producto_id_str in carrito:
        carrito[producto_id_str]['cantidad'] += 1
    else:
        carrito[producto_id_str] = {
            'nombre': producto.nombre,
            'precio': str(producto.precio),  # ⚠️ Convierte Decimal a str
            'cantidad': 1
        }

    request.session['carrito'] = carrito
    return redirect('carrito')  # O donde quieras redirigir



