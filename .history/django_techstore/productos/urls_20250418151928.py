from django.urls import path
from .views import index, detalle_producto,catalogo,categorias,carrito,añadir_producto
from django.conf import settings

urlpatterns = [
    path('', view=index, name='index'),
    path('producto/', detalle_producto, name='detalle_producto'),
    path('categoria/', categorias, name='categoria'),
    path('catalogo/', catalogo, name='catalogo'),
    path('carrito/', carrito, name="carrito")  
    path('carrito/aña/<int:producto_id>/', añadir_producto, name='añadir_al_carrito'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






