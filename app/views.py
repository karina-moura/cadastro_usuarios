from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import CLiente

# Create your views here.

class ClienteCreateView(CreateView):
    model = CLiente
    fields = "__all__"
    template_name = "form_cliente.html"
    success_url = "lista_clientes"


class ClienteListView(ListView):
    model = CLiente 
    template_name = "lista_clientes.html"

class ClienteDetailView(DetailView):
    model = CLiente
    template_name = "lista_cliente.html"
    context_object_name = "cliente"

class ClienteUpdateView(UpdateView):
    model = CLiente
    fields = "__all__"
    template_name = "form_cliente.html"
    success_url = reverse_lazy("lista_clientes")


class ClienteDeleteView(DeleteView):
    model = CLiente
    template_name = "remover_cliente.html"
    success_url = reverse_lazy("lista_clientes")

