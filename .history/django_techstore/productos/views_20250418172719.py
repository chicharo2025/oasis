from django.shortcuts import render, get_object_or_404 , redirect
from .models import Producto, Categoria
from django.contrib import messages



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

def categoria(request):
    producto = Producto.objects.all()
    return render(request, 'productos/categoria.html', {'productos': producto,})


def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'productos/catalogo.html', {'productos': productos,})

def carrito(request):
    productos = Producto.objects.all()
    return render(request, 'productos/carrito.html', {'productos': productos,})


def añadir_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    carrito = request.session.get('carrito', {})

    producto_id_str = str(producto.id)

    if producto_id_str in carrito:
        carrito[producto_id_str]['cantidad'] += 1
    else:
        carrito[producto_id_str] = {
            'nombre': producto.nombre,
            'precio': str(producto.precio),  
            'cantidad': 1
        }

    request.session['carrito'] = carrito
    return redirect('carrito') 



def restar_del_carrito(request, producto_id):
    # Verificamos si el carrito existe en la sesión
    carrito = request.session.get('carrito', {})

    # Verificamos si el producto está en el carrito
    if producto_id in carrito:
        # Restamos 1 al contador de unidades del producto
        carrito[producto_id] -= 1
        
        # Si la cantidad llega a cero, eliminamos el producto del carrito
        if carrito[producto_id] <= 0:
            del carrito[producto_id]
        
        # Guardamos el carrito actualizado en la sesión
        request.session['carrito'] = carrito
        
        # Mensaje para el usuario
        messages.success(request, f'El producto {producto_id} ha sido restado del carrito.')
    else:
        # Si el producto no está en el carrito
        messages.error(request, 'El producto no está en el carrito.')

    # Redirigimos al usuario a la página del carrito
    return redirect('carrito')  # Asegúrate de tener una vista llamada 'carrito'


