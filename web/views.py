from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Curso
from .forms import CursoForm, FormularioCursos, PeliculaForm, ContactoForm
from django.core.mail import send_mail
# Create your views here.


def index(request):
    """
        Homepage
    """
    cursos = Curso.objects.all()
    return render(request, "web/index.html", {"cursos": cursos})


def detallecurso(request, *args, **kwargs):
    """
        Devuelve el detalle de un curso usando la pk definida en urls.py.
    """
    curso = Curso.objects.get(pk=kwargs['pk'])
    formu = CursoForm()
    return render(
        request,
        "web/detalle_curso.html",
        {"curso": curso, "formu": formu})


def inscripciones(request, *args, **kwargs):
    if request.method == 'POST':
        formu = FormularioCursos(request.POST)
        if formu.is_valid():
            formu.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "web/inscripciones.html",
                {"form": formu, "error": formu.errors})
    else:
        formu = FormularioCursos()
        return render(request, "web/inscripciones.html", {"form": formu})


def contacto(request):
    """
        Renderiza la pagina de contacto con su formulario.
    """
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            send_mail(
                "EducIT: Recibimos tu mensaje",
                "Dentro de poco nos pondremos en contacto.",
                "contacto@educit.com.ar",
                [form.cleaned_data['email']],
                fail_silently=False,
            )
            form.save()
            return HttpResponseRedirect(reverse("contacto"))
        else:
            context = {'error': "El formulario no es valido"}
            return render(request, "web/contacto.html", context)
    else:
        form = ContactoForm()
        return render(request, "web/contacto.html", {"form": form})


def agregar_peliculas(request):
    """
        Renderiza un formulario para agregar peliculas
    """
    if request.method == "POST":
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("agregar_peliculas"))
        else:
            context = {'error': "El formulario no es valido"}
            return render(request, "web/agregar_pelicula.html", context)
    else:
        form = PeliculaForm()
        return render(request, "web/agregar_pelicula.html", {"form": form})
