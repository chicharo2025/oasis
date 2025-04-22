from django.contrib import admin
from .models import Producto, Categoria

admin.site.register(Producto)
admin.site.register(Categoria)

class Producto(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'categoria__nombre')