from django.shortcuts import render
from .models import *
from django.views.generic import *
from .forms import *
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.views import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class FormRegView(CreateView):
    model = User
    template_name = 'register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('final')

class FinalView(ListView):
    model = User
    template_name = 'final_page.html'