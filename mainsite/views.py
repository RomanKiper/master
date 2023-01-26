from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views.decorators.http import require_GET
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ContactForm, EmailBaseForm
from .models import Product, Contact, EmailBase, Category
from django.core.paginator import Paginator


class BaseMixin:
    context = {
        'instagram': 'https://instagram.com/stallain.by?igshid=NTdlMDg3MTY=',
        'facebook': 'https://www.facebook.com/',
    }


class CatalogListView(BaseMixin, ListView):
    paginate_by = 9
    template_name = "mainsite_new/catalog.html"
    context_object_name = "catalog"
    model = Product

    def get_queryset(self):
        return Product.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        return context


class MainPageCategoryView(BaseMixin, ListView):
    template_name = "mainsite_new/index.html"
    model = Category

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        return context


class MainPageProductNewView(BaseMixin, ListView):
    template_name = "mainsite_new/index.html"
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        return context


def main_page(request):
    product_new = Product.objects.filter(is_published=True, novelty=True )[:4]
    product_mostpopular = Product.objects.filter(is_published=True,)[:8]
    category = Category.objects.filter(is_published=True)

    response_data = {
        'product_new': product_new,
        'category': category,
        'product_mostpopular': product_mostpopular,
    }

    return render(request, 'mainsite_new/index.html', response_data)



class ProductDetailView(BaseMixin, DetailView):
    template_name = 'mainsite_new/product_main.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        return context


class AboutTemplateView(BaseMixin, TemplateView):
    template_name = "mainsite_new/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        context[
            'coordinate'] = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d10221.793301433216!2d27.54570734394003!3d53.906860922347065!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46dbcf94b327141f%3A0xd74e660de1f79fe9!2z0J3QtdC80LjQs9Cw!5e1!3m2!1sru!2sby!4v1671128718358!5m2!1sru!2sby'
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
    template_name = "mainsite_new/contact.html"
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('mainsite_products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        return context


class EmailCreateView(BaseMixin, CreateView):
    template_name = "mainsite_new/base.html"
    model = EmailBase
    form_class = EmailBaseForm
    success_url = reverse_lazy('mainsite_contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        return context



class Searchpanel(ListView):
    template_name = "mainsite_new/search_result.html"
    context_object_name = "news"
    model = Product


    def get_queryset(self):
        return Product.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context



def error404(request, exception):
    return render(request, "mainsite/error404.html")
