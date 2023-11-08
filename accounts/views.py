from django.shortcuts import render 
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView ,LogoutView
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class Login(LoginView):
    next_page = reverse_lazy('home')

class Logout(LogoutView):
    next_page = reverse_lazy('login')

class Register(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(Register,self).form_valid(form)

