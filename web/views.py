from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Curso
from .forms import CursoForm, FormularioCursos, PeliculaForm, ContactoForm, LoginForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


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
    """
        Renderiza el formulario de inscripción a un curso.
    """
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


def logueo(request):
    """
        Renderiza la pagina para identificarse a la web.
    """
    error = None
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            form = LoginForm()
            error = "El usuario no existe"
    else:
        form = LoginForm()
    return render(request, "web/login.html", {"form": form, "errors": error})


def deslogueo(request):
    """
        Realiza el deslogueo de la cuenta y redirige a la home.
    """
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def busqueda(request):
    """
        Devuelve resultados de busqueda hechos a traves del input del base.html.
    """
    cursos = Curso.objects.filter(nombre__contains=request.GET['q'])
    return render(request, "web/resultado_busqueda.html", {"cursos": cursos})

