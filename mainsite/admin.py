from django.contrib import admin

from .models import Category, Product, Contact, EmailBase, FilterAvailability, FilterPrice, Publication, \
    TypeOfPublications


@admin.action(description="Опубликовать")
def make_published(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description="Снять с публикации")
def make_unpublished(self, request, queryset):
    queryset.update(is_published=False)


class ProductInline(admin.StackedInline):
    model = Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    actions = (make_published, make_unpublished)
    list_display = ("name", "is_published",)
    list_filter = ("is_published",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(TypeOfPublications)
class TypeOfPublications(admin.ModelAdmin):
    actions = (make_published, make_unpublished)
    list_display = ("name", "is_published",)
    list_filter = ("is_published",)


@admin.register(FilterAvailability)
class FilterAvalabilityAdmin(admin.ModelAdmin):
    actions = (make_published, make_unpublished)
    list_display = ("name", "is_published",)
    list_filter = ("is_published",)


@admin.register(FilterPrice)
class FilterPriceAdmin(admin.ModelAdmin):
    actions = (make_published, make_unpublished)
    list_display = ("name", "is_published",)
    list_filter = ("is_published",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = (make_published, make_unpublished)
    search_fields = ("title", "price",)
    search_help_text = "Поиск по заголовку или цене"
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "price", "date_created_property", "date_update_property", "is_published",)
    list_editable = ("is_published", "price")
    list_filter = ("is_published", "category",)
    ordering = ("-date_created", "title")
    date_hierarchy = "date_created"
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "title", "descr", "category", "price", "filter_price", "filter_availability", "is_published"),
                "description": "Основные значения"
            }
        ),
        (
            "Дополнителные",
            {
                "fields": ("date_created", "author", "slug", "image", "novelty", "popularity",)
            }
        )
    )


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    actions = (make_published, make_unpublished)
    search_fields = ("title",)
    search_help_text = "Поиск по заголовку публикации"
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "date_created", "is_published",)
    list_editable = ("is_published",)
    list_filter = ("is_published", "type_of_publication",)
    ordering = ("-date_created", "title")
    date_hierarchy = "date_created"
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "title", "descr", "type_of_publication", "is_published"),
                "description": "Основные значения"
            }
        ),
        (
            "Дополнителные",
            {
                "fields": ("date_created", "slug", "image",)
            }
        )
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'is_published')
    list_editable = ('is_published',)
    search_fields = ("phone", "name",)
    search_help_text = "Поиск по имени"
    ordering = ("-date_created",)


@admin.register(EmailBase)
class EmailBaseAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_published',)
    list_editable = ('is_published',)
    search_fields = ('email',)
    search_help_text = 'Поиск по эллектронной почте'
    ordering = ('-date_created',)
