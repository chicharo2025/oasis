from django.urls import path
from .views import index, detalle_producto,catalogo,categorias
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', view=index, name='index'),
    path('producto/', detalle_producto, name='detalle_producto'),
    path('categoria/', categorias, name='categoria'),
    path('catalogo/', catalogo, name='catalogo'),
    path('agregar/<int:producto_id>/', agregar_producto, name="AgregarProducto"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="EliminarProducto"),
    path('restar/<int:producto_id>/', restar_producto, name="RestarProducto"),
    path('limpiar/', limpiar_carrito, name="LimpiarCarrito"),
    
  
  
   

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






