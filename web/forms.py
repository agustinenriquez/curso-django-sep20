from .models import Curso, Pelicula
from django import forms


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
    fecha_estreno = forms.DateField(input_formats=['%d-%m-%Y'])

    class Meta:
        model = Pelicula
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PeliculaForm, self).__init__(*args, **kwargs)
        self.fields['mayores_de'].initial = None
