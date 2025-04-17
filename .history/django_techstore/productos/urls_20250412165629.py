from django.urls import path
from .views import index, detalle_producto, 


urlpatterns = [
       
    path('', index, name='index'),
    path('producto/<int:id_productos>/', detalle_producto, name='detalle_producto'),
    path('categorias/', views.categoria, name='categoria'),
    path('productos/', views.producto, name='producto'),
]
