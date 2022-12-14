from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views.decorators.http import require_GET
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ContactForm, Myform
from .models import Product, Contact


class BaseMixin:
    context = {
        'instagram': 'https://instagram.com/stallain.by?igshid=NTdlMDg3MTY=',
        'facebook': 'https://www.facebook.com/',
    }


class MainsiteListView(BaseMixin, ListView):
    template_name = "mainsite/index.html"
    context_object_name = "products"
    model = Product

    def get_queryset(self):
        return Product.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['heading'] = "+++BOGDANSITE+++"
        context['subheading'] = 'ручная работа'
        context.update(self.context)
        context['form'] = ContactForm()
        context['my_form'] = Myform()
        return context

    def post(self, request: HttpRequest):
        if request.POST.get('contact_form_2') == "contact_form":
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
        elif request.POST.get('contact_form_2') == "email_form":                #or "phone_form"::
            print(request.POST.get('email'))

        return self.get(request=request)


class ProductDetailView(BaseMixin, DetailView):
    template_name = 'mainsite/post.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        return context


class AboutTemplateView(LoginRequiredMixin, BaseMixin, TemplateView):
    template_name = "mainsite/about.html"
    login_url = "signin"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        context['heading'] = 'about us'
        context['coordinate'] = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d10221.793301433216!2d27.54570734394003!3d53.906860922347065!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46dbcf94b327141f%3A0xd74e660de1f79fe9!2z0J3QtdC80LjQs9Cw!5e1!3m2!1sru!2sby!4v1671128718358!5m2!1sru!2sby'
        context['about'] = '''
        ABOUT ABOUT ABOUT ABOUT        
        ABOUT ABOUT ABOUT ABOUT        
        ABOUT ABOUT ABOUT ABOUT        
        ABOUT ABOUT ABOUT ABOUT        
        ABOUT ABOUT ABOUT ABOUT        
        ABOUT ABOUT ABOUT ABOUT                
        '''
        return context


class ContactCreateView(BaseMixin, CreateView):
    template_name = "mainsite/contact.html"
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('mainsite_products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        context['heading'] = 'Свяжитесь с нами, иначе мы найдем вас )'
        return context


def error404(request, exception):
    return render(request, "mainsite/error404.html")
