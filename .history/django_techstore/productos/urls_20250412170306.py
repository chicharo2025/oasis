from django.urls import path
from .views import index, detalle_producto


urlpatterns = [
       
    path('', index, name='index'),
    path('producto/<int:id_productos>/', detalle_producto, name='detalle_producto'),
    path('categoria/',  name='categoria'),
    path('catalogo/', views.catalogo, name='catalogo'),
]
