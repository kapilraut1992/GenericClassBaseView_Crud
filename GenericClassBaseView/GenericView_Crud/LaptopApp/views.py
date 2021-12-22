from django.shortcuts import render
from .models import Laptop
from django.views.generic import CreateView,ListView,UpdateView,DeleteView

# Create your views here.

class Laptop_add(CreateView):
    model=Laptop
    fields='__all__'
    success_url='/laptop/show'

class Laptop_show(ListView):
    model=Laptop


class Laptop_update(UpdateView):
    model=Laptop
    fields='__all__'
    success_url='/laptop/show'

class Laptop_delete(DeleteView):
    model=Laptop
    fields='__all__'
    success_url='/laptop/show'