from django.test import TestCase

# Create your tests here.
# Antes (si verificabas producto.html)
self.assertTemplateUsed(response, 'productos/producto.html')

# Ahora (si cambiaste a catalogo.html)
self.assertTemplateUsed(response, 'productos/catalogo.html')