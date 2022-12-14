from django.urls import path

from .views import mainsite_list, product_detail

urlpatterns = [
    path("", mainsite_list, name = 'mainsite_products'),
    path("<slug:product_slug>/", product_detail, name="mainsite_product")
]