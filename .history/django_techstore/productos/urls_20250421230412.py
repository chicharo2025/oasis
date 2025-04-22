from django.urls import path
from .views import index, lista, detalle_producto,catalogo,carrito,añadir_al_carrito,restar_del_carrito
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('', view=index, name='index'),
    path('producto/<int:producto_id>/', detalle_producto, name='detalle_producto'),
    path('catalogo/', catalogo, name='catalogo'),
    path('carrito/', carrito, name="carrito"), 
    path('productos/', lista, name='lista'), 
    path('añadir/<int:producto_id>/', añadir_al_carrito, name='añadir_al_carrito'),
    path('restar/<int:producto_id>/', restar_del_carrito, name='restar_del_carrito'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




from django.urls import path
from . import views

app_name = 'productos'

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
]

