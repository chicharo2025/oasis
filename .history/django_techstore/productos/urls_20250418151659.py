from django.urls import path
from .views import index, detalle_producto,catalogo,categorias,carrito

from django.conf import settings

urlpatterns = [
    path('', view=index, name='index'),
    # proyecto/urls.py
path('tienda/', include(('tienda.urls', 'tienda'), namespace='tienda')),

    path('producto/', detalle_producto, name='detalle_producto'),
    path('categoria/', categorias, name='categoria'),
    path('catalogo/', catalogo, name='catalogo'),
    path('carrito/', carrito, name="carrito")  
    
    path('carrito/agregar/<int:producto_id>/', views.añadir_al_carrito, name='añadir_al_carrito'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






