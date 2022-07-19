from django.test import TestCase


class TestViews(TestCase):
    """
    Test cases for products app views
    """

    def test_products_page(self):
        """ Test products page loads """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_products_details_page(self):
        """ Test product details page loads """
        response = self.client.get('/products/2/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
