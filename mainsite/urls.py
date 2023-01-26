from django.urls import path

from .views import main_page, ContactCreateView, ProductDetailView, MainPageCategoryView, AboutTemplateView, CatalogListView, Searchpanel


urlpatterns = [
    path("", main_page, name='mainsite_products'),
    path("contact/", ContactCreateView.as_view(), name="mainsite_contact"),
    path("about/", AboutTemplateView.as_view(), name="mainsite_about" ),
    path("catalog/", CatalogListView.as_view(), name = 'mainsite_catalog'),
    path("search/", Searchpanel.as_view(), name = 'search'),
    path("<slug:product_slug>/", ProductDetailView.as_view(), name="mainsite_product")
]