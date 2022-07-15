from django.test import TestCase


class TestViews(TestCase):
    """
    Test cases for home app view
    """

    def test_home_page(self):
        """ Test home page loads """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
