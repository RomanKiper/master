from django.urls import path

from .views import contact, ProductDetailView, MainsiteListView

urlpatterns = [
    path("", MainsiteListView.as_view(), name = 'mainsite_products'),
    path("contact/", contact, name="mainsite_contact"),
    path("<slug:product_slug>/", ProductDetailView.as_view(), name="mainsite_product")
]