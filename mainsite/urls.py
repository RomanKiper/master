from django.urls import path

from .views import ContactCreateView, ProductDetailView, MainsiteListView, AboutTemplateView

urlpatterns = [
    path("", MainsiteListView.as_view(), name = 'mainsite_products'),
    path("contact/", ContactCreateView.as_view(), name="mainsite_contact"),
    path("about/", AboutTemplateView.as_view(), name="mainsite_about" ),
    path("<slug:product_slug>/", ProductDetailView.as_view(), name="mainsite_product")
]