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
from django.test import TestCase
from web.models import Contacto
# Create your tests here.


class ContactoModelTest(TestCase):

    def test_instanciate_contacto_model_ok(self):
        contacto = Contacto()
        self.assertTrue(isinstance(contacto, Contacto))

    def test_instanciate_contacto_with_author(self):
        contacto = Contacto()
        contacto.author = "TestAuthor"
        self.assertTrue(isinstance(contacto, Contacto))
        self.assertTrue(contacto.author, "TestAuthor")

    def test_instanciate_contacto_with_fields(self):
        author = "testAuthor"
        email = "test@test.com"
        mensaje = "esto es un mensaje de testeo."
        contacto = Contacto(
            author=author,
            email=email,
            mensaje=mensaje)
        self.assertTrue(isinstance(contacto, Contacto))
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
