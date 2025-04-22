from django.urls import path
from .views import index, detalle_producto,catalogo,categorias,ver_carrito,añadir_al_carrito,quitar_del_carrito
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', view=index, name='index'),
    path('producto/', detalle_producto, name='detalle_producto'),
    path('categoria/', categoria, name='categoria'),
    path('catalogo/', catalogo, name='catalogo'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('carrito/añadir/<int:producto_id>/', añadir_al_carrito, name='añadir_al_carrito'),
    path('quitar/<int:producto_id>/', quitar_del_carrito, name='quitar_del_carrito'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






