from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

from .models import Product

@require_GET
def mainsite_list(request: HttpRequest):
    products_lists = Product.objects.all()
    return render(request, "mainsite/index.html", {"products": products_lists})

def product_detail(request: HttpRequest, product_slug: str):
    product = get_object_or_404(Product, slug=product_slug )
    # product = Product.objects.get(slug=product_slug)
    return render(request, "mainsite/post.html", {"product": product})

def error404(request, exception):
    return render(request, "mainsite/error404.html")



