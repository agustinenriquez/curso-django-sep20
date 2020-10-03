from .models import Curso, Pelicula, Contacto
from django import forms
from django.contrib.auth.models import User


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'


class FormularioCursos(forms.Form):
    TURNOS = (('NOCHE', 'noche'), ('TARDE', 'tarde'), ('MAÑANA', 'mañana'))
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    telefono = forms.IntegerField(label="Telefono", required=False)
    email = forms.EmailField(required=False)
    es_empresa = forms.BooleanField(label="Es empresa?", required=False)
    turno = forms.ChoiceField(choices=TURNOS, required=False)
    fecha_inicio = forms.DateField(label="Fecha de inicio", input_formats=["%d/%m/%y"])

    def __str__(self):
        return self.nombre


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ("username", "password")


class UserForm(forms.Form):
    usuario = forms.CharField(label="Nombre", max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
