from django.urls import path

from .views import ContactCreateView, ProductDetailView, MainPageView, AboutTemplateView, CatalogListView, PublicationListView, PublicationDetailView


urlpatterns = [
    path("", MainPageView.as_view(), name='mainsite_products'),
    path("contact/", ContactCreateView.as_view(), name="mainsite_contact"),
    path("about/", AboutTemplateView.as_view(), name="mainsite_about" ),
    path("catalog/", CatalogListView.as_view(), name = 'mainsite_catalog'),
    path("publications/", PublicationListView.as_view(), name="mainsite_publications"),
    path("product/<slug:product_slug>/", ProductDetailView.as_view(), name="mainsite_product"),
    path("publication/<slug:publication_slug>/", PublicationDetailView.as_view(), name="mainsite_publication")
]