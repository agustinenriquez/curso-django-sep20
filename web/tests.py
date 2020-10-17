import django; django.setup()
from unittest import TestCase
from web.models import Contacto


class HomeTest(TestCase):

    def setUp(self):
        self.url = "/"

    def test_homepage(self):
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, 200)

    def test_contacto(self):
        instance = Contacto()
        self.assertEqual(type(instance.author), str)
