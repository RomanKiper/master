from django.contrib.auth.views import LoginView, TemplateView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterForm, Loginform


class RegisterCreateView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('signin')


class SignInView(LoginView):
    form_class = Loginform
    template_name = 'registration/signin.html'
    success_url = reverse_lazy('mainsite_products')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile.html'
    login_url = '/signin/'
