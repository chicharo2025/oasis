from django.urls import path
from .views import index, detalle_producto
from . import views

urlpatterns = [
       
    path('', index, name='index'),
    path('producto/<int:id_productos>/', detalle_producto, name='detalle_producto'),
    path('categoria/', views.categoria, name='categoria'),
    path('producto/', views.catalogo, name='catalogo'),
]


