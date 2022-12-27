from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views.decorators.http import require_GET
from .forms import ContactForm
from .models import Product


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
        return context


class ProductDetailView(BaseMixin, DetailView):
    template_name = 'mainsite/post.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        return context


# @require_GET
# def mainsite_list(request: HttpRequest):
#     products_lists = Product.objects.all()
#     return render(request, "mainsite/index.html", {"products": products_lists})

# def product_detail(request: HttpRequest, product_slug: str):
#     product = get_object_or_404(Product, slug=product_slug)
#     # product = Product.objects.get(slug=product_slug)
#     return render(request, "mainsite/post.html", {"product": product})


def contact(request: HttpRequest):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request, "mainsite/contact.html", {"contact_form": form})


def error404(request, exception):
    return render(request, "mainsite/error404.html")
