from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Curso
from .forms import CursoForm, FormularioCursos, LoginForm, PeliculaForm, ContactoForm, UsuarioForm
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
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
    adjuntos = AdjuntosCurso.objects.filter(curso__id=curso.id)
    return render(
        request,
        "web/detalle_curso.html",
        {"curso": curso, "formu": formu, "adjuntos": adjuntos})


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
    context = {}
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            # send_mail(
            #     "EducIT: Recibimos tu mensaje",
            #     "Dentro de poco nos pondremos en contacto.",
            #     "contacto@educit.com.ar",
            #     [form.cleaned_data['email']],
            #     fail_silently=False,
            # )
            form.save()
            return HttpResponseRedirect(reverse("contacto"))
        else:
            messages.add_message(request, messages.INFO, 'El formulario no es valido')
            context["form"] = ContactoForm()
            context['error'] = "El formulario no es valido"
            context["author_field_error"] = form.errors['author'][0]
            return render(request, "web/contacto.html", context)
    else:
        messages.add_message(request, messages.INFO, 'GET REQUEST.')
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


def busqueda(request):
    """
        Devuelve resultados de busqueda hecho a traves del formulario.
        Curso.objects.all() -> devuelve todos los resultados
        Curso.objects.first() -> primero
        Curso.objects.last() -> ultimo
        Curso.objects.distinct() -> elimina duplicados
        Curso.objects.all().delete() -> borra todo
        Curso.objects.first().delete() -> borra uno
        Curso.objects.all[0].delete()
        Curso.objects.get(pk=1) -> devuelve obj con pk 1
        Contacto.objects.filter(mensaje__contains="texto")
        Curso.objects.get(pk=1).values("nombre") -> devuelve el campo seleccionado
        Perfil.objects.filter(user__email__contains="@gmail.com")

        *** Subfiltros ***

        __contains __icontains __in __field __lte __gte __lt __gt
        __exact __endswith __isnull 

        ***            ***

        Perfil.objects.all().exclude()

        Q queries | F Expressions
        prefetch_related | select_related

    """
    curso = Curso.objects.filter(nombre__icontains=request.GET['q'])
    return render(request, "web/resultados_busqueda.html", {'cursos': curso})


def logueo(request):
    """
        Renderiza la pagina para identificarse a la web.
    """
    error = None
    if request.method == "POST":
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
    return render(request, "web/login.html", {"form": form, "error": error})


def deslogueo(request):
    """
        Desloguea al usuario y redirecciona a la home.
    """
    logout(request)
    return HttpResponseRedirect(reverse("index"))


@login_required(login_url="/login/")
def crear_curso(request):
    """
        Renderiza el formulario de creacion de cursos.
    """
    error = None
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("crear-curso"))
        else:
            context = {'error': "El formulario no es valido"}
            return render(request, "web/agregar_pelicula.html", context)
    else:
        form = CursoForm()
    return render(request, "web/crear_curso.html", {"form": form, "error": error})


def crear_usuario(request):
    """
        Renderiza formulario para crear un usuario.
    """
    template = "web/crear_usuario.html"
    context = {}
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            obj, created = User.objects.get_or_create(
                username=request.POST['username'],
                password=request.POST['password'],
                email=request.POST['email'])
            if created:
                return HttpResponseRedirect(reverse("index"))
            else:
                context['form'] = UsuarioForm()
                context["ya_creado"] = True
                return render(request, template, context)
        else:
            context['error'] = 'el usuario ya existe.'
            return render(request, template, context)
    else:
        context['form'] = UsuarioForm()
        return render(request, template, context)
