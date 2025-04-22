from django.urls import path
from .views import index, detalle_producto,catalogo,categorias,carrito,añadir_al_carrito,restar_del_carrito,productos_por_categoria
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('', view=index, name='index'),
    path('producto/<int:producto_id>/', detalle_producto, name='detalle_producto'),
   Page not found (404)
Request Method:	GET
Request URL:	http://127.0.0.1:8000/categoria/
Using the URLconf defined in django_techstore.urls, Django tried these URL patterns, in this order:

admin/
[name='index']
producto/<int:producto_id>/ [name='detalle_producto']
categorias/<int:categoria_id>/ [name='categorias']
categorias/<int:categoria_id>/ [name='productos_por_categoria']
catalogo/ [name='catalogo']
carrito/ [name='carrito']
añadir/<int:producto_id>/ [name='añadir_al_carrito']
restar/<int:producto_id>/ [name='restar_del_carrito']
^media/(?P<path>.*)$
^media/(?P<path>.*)$
The current path, categoria/, didn’t match any of these.

You’re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard 404 page.
    path('catalogo/', catalogo, name='catalogo'),
    path('carrito/', carrito, name="carrito"),  
    path('añadir/<int:producto_id>/', añadir_al_carrito, name='añadir_al_carrito'),
    path('restar/<int:producto_id>/', restar_del_carrito, name='restar_del_carrito'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






