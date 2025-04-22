from django.urls import path
from .views import index, detalle_producto,catalogo,categorias,carrito,añadir_al_carrito,restar_del_carrito,productos_por_categoria
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('', view=index, name='index'),
    path('producto/<int:producto_id>/', detalle_producto, name='detalle_producto'),
   
    path('catalogo/', catalogo, name='catalogo'),
    path('carrito/', carrito, name="carrito"),  
    path('añadir/<int:producto_id>/', añadir_al_carrito, name='añadir_al_carrito'),
    path('restar/<int:producto_id>/', restar_del_carrito, name='restar_del_carrito'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






