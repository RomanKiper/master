from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views.decorators.http import require_GET
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ContactForm, EmailBaseForm
from .models import Product, Contact, EmailBase, Category, FilterAvailability, FilterPrice, Publication
from django.core.paginator import Paginator


class BaseMixin:
    context = {
        'instagram': 'https://instagram.com/stallain.by?igshid=NTdlMDg3MTY=',
        'facebook': 'https://www.facebook.com/',
        'form_email': EmailBaseForm(),
    }

    def post(self, request):
        form = EmailBaseForm(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request)



class CatalogListView(BaseMixin, ListView):
    paginate_by = 9
    template_name = "mainsite_new/catalog_list.html"
    context_object_name = "catalog"
    model = Product

    def get_queryset(self):
        return Product.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        filter_price = FilterPrice.objects.filter(is_published=True)
        filter_availability = FilterAvailability.objects.filter(is_published=True, )
        category = Category.objects.filter(is_published=True)


        context.update({
            'filter_price': filter_price,
            'category': category,
            'filter_availability': filter_availability,
        })
        return context




class PublicationListView(BaseMixin, ListView):
    template_name = "mainsite_new/publications_list.html"
    context_object_name = "publications"
    model = Publication

    def get_queryset(self):
        return Publication.objects.filter(is_published=True,).order_by('-date_created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        return context


class MainPageView(BaseMixin, ListView):
    template_name = "mainsite_new/index.html"
    model = Category

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        product_new = Product.objects.filter(is_published=True, novelty=True)[:4]
        category = Category.objects.filter(is_published=True)
        product_mostpopular = Product.objects.filter(is_published=True, popularity=True)[:8]

        context.update({
            'product_new': product_new,
            'category': category,
            'product_mostpopular': product_mostpopular,
        })
        return context


class PublicationDetailView(BaseMixin, DetailView):
    template_name = 'mainsite_new/publication_main.html'
    context_object_name = 'publication'
    slug_url_kwarg = 'publication_slug'
    model = Publication

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        publication_latest = Publication.objects.filter(is_published=True)[:8]

        context.update({
            'publication_latest': publication_latest,
        })
        return context


class ProductDetailView(BaseMixin, DetailView):
    template_name = 'mainsite_new/product_main.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        product_mostpopular = Product.objects.filter(is_published=True, novelty=True)[:4]

        context.update({
            'product_mostpopular': product_mostpopular,
        })

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
        context['form'] = ContactForm()
        context['form_email'] = EmailBaseForm()
        return context

    def post(self, request: HttpRequest):
        if request.POST.get('form_type') == 'sentContact':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
        elif request.POST.get('form_tipe') == 'sentMessage':
            print(request.POST.get('form_email'))
        return self.get(request=request)


class EmailCreateView(BaseMixin, CreateView):
    template_name = "mainsite_new/base.html"
    model = EmailBase
    form_class = EmailBaseForm
    success_url = reverse_lazy('mainsite_contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        return context


class FilterProductView(CatalogListView, ListView):

    def get_queryset(self):
        queryset = Product.objects.filter(
            Q(category__in=self.request.GET.getlist("category")) |
            Q(filter_price__in=self.request.GET.getlist("filter_price")) |
            Q(filter_availability__in=self.request.GET.getlist("filter_availability"))
        )
        return queryset


def error404(request, exception):
    return render(request, "mainsite/error404.html")



