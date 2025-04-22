from django.urls import path
from .views import index, detalle_producto,catalogo,categorias,carrito,añadir_al_carrito
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('', view=index, name='index'),
    path('producto/<int:producto_id>/', detalle_producto, name='detalle_producto'),
    path('categoria/', categorias, name='categoria'),
    path('catalogo/', catalogo, name='catalogo'),
    path('carrito/', carrito, name="carrito"),  
        path('añadir/<int:producto_id>/', views.añadir_al_carrito, name='añadir_al_carrito'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






