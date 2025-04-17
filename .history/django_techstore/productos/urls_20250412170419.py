from django.urls import path
from .views import index, detalle_producto
from . import views

urlpatterns = [
       
    path('', index, name='index'),
    path('producto/<int:id_productos>/', detalle_producto, name='detalle_producto'),
   path('categorias/', views.categoria, name='categoria'),
    path('productos/', views.producto, name='producto'),
]


from django.urls import path
from . import views  # Importa las vistas de la app actual

urlpatterns = [
    path('categorias/', views.categoria, name='categoria'),
    path('productos/', views.producto, name='producto'),
]