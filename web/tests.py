import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cursodjango.settings")
import django; django.setup()
from django.test import TestCase
from web.models import Contacto


class HomeTest(TestCase):

    def setUp(self):
        self.url = "/"

    def test_homepage(self):
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, 200)


class ContactoModelTest(TestCase):

    def setup(self):
        self.instance = Contacto()

    def test_instanciate_contacto_model_ok(self):
        self.assertTrue(isinstance(self.instance, Contacto))

    def test_instanciate_contacto_with_author(self):
        self.instance
        self.instance.author = "TestAuthor"
        self.assertTrue(self.instance.author, "TestAuthor")

    def test_instanciate_contacto_with_fields(self):
        author = "testAuthor"
        email = "test@test.com"
        mensaje = "esto es un mensaje de testeo."
        contacto = Contacto(
            author=author,
            email=email,
            mensaje=mensaje)
        self.assertTrue(contacto.author, mensaje)
        self.assertTrue(contacto.email, email)
        self.assertTrue(contacto.mensaje, mensaje)

    def test_contacto_with_invalid_email_two_ats(self):
        contacto = Contacto(
            author="testAuthor",
            email="test@@test.com.er",
            mensaje="esto es un mensaje de test")
        self.assertTrue(contacto, Contacto)
        self.assertGreater(contacto.email.count("@"), 1)

    def test_contacto_author_isdecimal_isdigit(self):
        contacto = Contacto(
            author=123,
            email="test@@test.com.er",
            mensaje="esto es un mensaje")
        self.assertTrue(contacto, Contacto)
        self.assertTrue(type(contacto.author) == int)
