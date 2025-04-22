from django.shortcuts import render,redirect, get_object_or_404
from .models import Producto, Categoria

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
    return render(request, 'productos/categoria.html', {
        'ca': categorias
    })


def catalogo(request):
    productos = Producto.objects.all()
    
    return render(request, 'productos/catalogo.html', {'productos': productos,})


def añadir_al_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    carrito[str(producto_id)] = carrito.get(str(producto_id), 0) + 1
    request.session['carrito'] = carrito
    return redirect('ver_carrito')

def quitar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    if str(producto_id) in carrito:
        del carrito[str(producto_id)]
    request.session['carrito'] = carrito
    return redirect('ver_carrito')

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos = []
    total = 0

    for id_str, cantidad in carrito.items():
        producto = get_object_or_404(Producto, id=int(id_str))
        subtotal = producto.precio * cantidad
        total += subtotal
        productos.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal
        })

    return render(request, 'productos/carrito.html', {'productos': productos, 'total': total})
