from django.contrib.messages.api import success
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Curso, Contacto, Inscripcion
from .forms import CursoForm, FormularioCursos, LoginForm, PeliculaForm, ContactoForm, UsuarioForm
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
import logging
from django.views.generic.base import TemplateView
from django.views.generic import FormView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = "web/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["saludo"] = "hola hola"
        return context


class ContactView(FormView):
    form_class = ContactoForm
    success_url = "/contacto/"
    template_name = "web/contacto.html"

    def form_valid(self, form):
        Contacto.objects.create(
            author=form.cleaned_data['author'],
            mensaje=form.cleaned_data['mensaje'],
            email=form.cleaned_data['email']
        )
        return HttpResponseRedirect(self.success_url)


class ContactoListView(ListView):
    model = Contacto
    template_name = "web/lista_mensajes.html"
    queryset = Contacto.objects.filter(created_date__isnull=False).order_by("-created_date")



class CursoListView(ListView):
    model = Curso


class CursoDetailView(DetailView):
    model = Curso


class InscripcionesCreateView(LoginRequiredMixin, CreateView):
    model = Inscripcion
    template_name = "web/inscripciones.html"
    fields = ("nombre", "email", "curso")
    success_url = "/"

    def get_success_url(self):
        return f"{self.success_url}"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        if "form" not in kwargs:
            form = self.get_form()
            items = form.fields['curso'].choices.queryset.filter(pk=self.kwargs["pk"])
            form.initial["curso"] = items.first()
        return super().get_context_data(**kwargs)


class UpdateCurso(UpdateView):
    model = Curso
    form_class = CursoForm
    success_url = "/curso/"

    def get_success_url(self):
        return f"{self.success_url}{self.object.id}"
