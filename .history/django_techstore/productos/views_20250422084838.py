from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria
from django.contrib import messages
from decimal import Decimal
from django.views.generic import ListView
from django.db.models import Q
from django.http import JsonResponse

def index(request):
    categorias = Categoria.objects.all()
    productos_oferta = Producto.objects.filter(en_oferta=True)
    productos = Producto.objects.filter(destacado=True)[:4]
    return render(request, 'productos/index.html', {
        'categorias': categorias,
        'productos_oferta': productos_oferta,
        'productos': productos,
    })

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'productos/detalle.html', {'producto': producto})

def lista(request):
    categoria_id = request.GET.get('categoria')
    categorias = Categoria.objects.all()
    
    if categoria_id:
        productos = Producto.objects.filter(categorias__id=categoria_id)
    else:
        productos = Producto.objects.all()
    
    return render(request, 'productos/lista.html', {
        'productos': productos,
        'categorias': categorias
    })
def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'productos/catalogo.html', {'productos': productos})

def carrito(request):
    carrito = request.session.get('carrito', {})
    
    # Preparar los datos del carrito para la plantilla
    items_carrito = []
    total = Decimal('0.00')
    
    for producto_id, item in carrito.items():
        producto = get_object_or_404(Producto, id=producto_id)
        subtotal = Decimal(item['precio']) * item['cantidad']
        total += subtotal
        
        items_carrito.append({
            'producto': producto,
            'cantidad': item['cantidad'],
            'subtotal': subtotal,
            'id': producto_id
        })
    
    return render(request, 'productos/carrito.html', {
        'items_carrito': items_carrito,
        'total': total
    })

def añadir_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    carrito = request.session.get('carrito', {})
    
    producto_id_str = str(producto.id)
    
    if producto_id_str in carrito:
        carrito[producto_id_str]['cantidad'] += 1
        messages.success(request, f'Cantidad de {producto.nombre} actualizada en el carrito')
    else:
        carrito[producto_id_str] = {
            'nombre': producto.nombre,
            'precio': str(producto.precio),
            'cantidad': 1,
            'imagen': producto.imagen.url if producto.imagen else ''
        }
        messages.success(request, f'{producto.nombre} añadido al carrito')
    
    request.session['carrito'] = carrito
    return redirect(request.META.get('HTTP_REFERER', 'catalogo'))

def restar_del_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto_id_str = str(producto_id)
    
    carrito = request.session.get('carrito', {})
    
    if producto_id_str in carrito:
        if carrito[producto_id_str]['cantidad'] > 1:
            carrito[producto_id_str]['cantidad'] -= 1
            messages.success(request, f'Cantidad de {producto.nombre} reducida en el carrito')
        else:
            del carrito[producto_id_str]
            messages.success(request, f'{producto.nombre} eliminado del carrito')
        
        request.session['carrito'] = carrito
    else:
        messages.error(request, 'El producto no está en el carrito')
    
    return redirect('carrito')

def eliminar_del_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto_id_str = str(producto_id)
    
    carrito = request.session.get('carrito', {})
    
    if producto_id_str in carrito:
        del carrito[producto_id_str]
        messages.success(request, f'{producto.nombre} eliminado del carrito')
        request.session['carrito'] = carrito
    else:
        messages.error(request, 'El producto no está en el carrito')
    
    return redirect('carrito')

def limpiar_carrito(request):
    if 'carrito' in request.session:
        del request.session['carrito']
        messages.success(request, 'Carrito vaciado correctamente')
    return redirect('carrito')



# Vista (views.py)
class ProductSearchView(ListView):
    model = Producto
    template_name = "productos/productos_catalogo.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Producto.objects.filter(nombre__icontains=query) if query else []

def product_autocomplete(request):
    if 'term' in request.GET:
        query = request.GET.get('term', '')
        products = Producto.objects.filter(name__icontains=query)[:10]
        results = [{
            'label': p.name, 
            'value': p.name, 
            'url': p.get_absolute_url()
        } for p in products]
        return JsonResponse(results, safe=False)
    return JsonResponse([], safe=False)

def buscar(request):
    query = request.GET.get('q')
    productos = Producto.objects.filter(nombre__icontains=query) if query else []
    return render(request, 'productos/buscar.html', {'productos': productos})