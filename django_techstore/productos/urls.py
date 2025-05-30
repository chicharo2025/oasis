from django.conf.urls.static import static 
from django.conf import settings
from . import views
from .views import ProductoSearchView, producto_autocomplete
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('lista/', views.lista, name='lista'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('carrito/', views.carrito, name='carrito'),
    path('añadir-al-carrito/<int:producto_id>/', views.añadir_al_carrito, name='añadir_al_carrito'),
    path('restar-del-carrito/<int:producto_id>/', views.restar_del_carrito, name='restar_del_carrito'),
    path('eliminar-del-carrito/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('limpiar-carrito/', views.limpiar_carrito, name='limpiar_carrito'),
    path('catalogo/', ProductoSearchView.as_view(), name='product_search'),
    path('autocomplete/', producto_autocomplete, name='product_autocomplete'),
    path('buscar/', views.buscar, name='buscar'),
    path('pago/', views.pago, name='pago')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

