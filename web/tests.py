import django
from django.core.exceptions import ValidationError; django.setup()
from unittest import TestCase
from web.models import Contacto
from model_bakery import baker


class ContactoModelTest(TestCase):
    def setUp(self):
        self.contacto = baker.make('web.Contacto')
        print(self.contacto)

    def test_instanciate_contacto_model_ok(self):
        self.assertTrue(isinstance(self.contacto, Contacto))

    def test_instanciate_contacto_with_author(self):
        self.contacto.author = "TestAuthor"
        self.assertTrue(self.contacto.author, "TestAuthor")

    def test_instanciate_contacto_with_fields(self):
        author = "testAuthor"
        email = "test@test.com"
        mensaje = "esto es un mensaje de testeo."
        self.contacto.author = author
        self.contacto.email = email
        self.contacto.mensaje = mensaje
        self.assertTrue(self.contacto.author, mensaje)
        self.assertTrue(self.contacto.email, email)
        self.assertTrue(self.contacto.mensaje, mensaje)

    def test_contacto_with_invalid_email_two_ats(self):
        self.contacto.author = "testAuthor",
        self.contacto.email = "test@@test.com.er",
        self.contacto.mensaje = "esto es un mensaje de test"
        self.assertGreater(self.contacto.email[0].count("@"), 1)

    def test_contacto_with_invalid_email_two_ats_exception(self):
        self.contacto.author = "testAuthor",
        self.contacto.email = "test@@test.com.er",
        self.contacto.mensaje = "esto es un mensaje de test"
        self.assertGreater(self.contacto.email[0].count("@"), 1)
        with self.assertRaises(ValidationError):
            self.contacto.validate_email(self.contacto.email[0])
            

    def test_contacto_author_isdecimal_isdigit(self):
        contacto = Contacto(
            author=123,
            email="test@test.com.er",
            mensaje="esto es un mensaje")
        self.assertTrue(type(contacto.author) == int)
