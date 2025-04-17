from django.test import TestCase
from django.urls import reverse

class ProductViewTests(TestCase):
    def test_product_view_uses_correct_template(self):
        # Make a GET request to the product view
        response = self.client.get(reverse('producto'))  # Assuming 'producto' is the URL name
        
        # Verify that the correct template is used
        self.assertTemplateUsed(response, 'productos/catalogo.html')