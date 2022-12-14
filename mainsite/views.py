from django.http import HttpRequest
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.decorators.http import require_GET

from .models import Product

def mainsite_list(request: HttpRequest):
    return render(request, "mainsite/product_list.html")

def product_detail(request: HttpRequest, product_slug: str):
    product = get_object_or_404(Product, slug=product_slug )
    # product = Product.objects.get(slug=product_slug)
    return HttpResponse(f"<br><br><b>{product.title}</b>")

def error404(request, exception):
    return render(request, "mainsite/error404.html")



