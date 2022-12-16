from django.contrib import admin

from .models import Category, Product


@admin.action(description="Опубликовать")
def make_published(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description="Снять с публикации")
def make_unpublished(self, request, queryset):
    queryset.update(is_published=False)


class ManagerPanel(admin.AdminSite):
    site_header = "Manager panel"
    site_title = "Manager"
    index_title = "Manager index"

manager = ManagerPanel(name="manager")


class ProductInline(admin.StackedInline):
    model = Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    actions = (make_published, make_unpublished)
    inlines = (ProductInline,)
    list_display = ("name", "is_published",)
    list_filter = ("is_published",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = (make_published, make_unpublished)
    search_fields = ("title", "price",)
    search_help_text = "Поиск по заголовку или цене"
    prepopulated_fields = {"slug": ("title", )}
    list_display = ("title", "price", "date_created_property", "date_update_property", "is_published",)
    list_editable = ("is_published", "price")
    list_filter = ("is_published", "category",)
    ordering = ("-date_created", "title")
    date_hierarchy = "date_created"
    fieldsets = (
        (
            "Основное",
            {
                "fields": ("title", "descr", "category", "price", "is_published" ),
                "description": "Основные значения"

            }
        ),
        (
            "Дополнителные",
            {
                "fields": ("date_created", "author", "slug")
            }

        )
    )

# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Product, ProductAdmin)
manager.register(Category, CategoryAdmin)
manager.register(Product, ProductAdmin)
