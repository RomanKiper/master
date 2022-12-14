from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(
        max_length=64,
        null=True,
        unique=True,
        verbose_name="название",
        help_text="Макс. 64 символа"
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name="публикация",
    )
    slug = models.SlugField(verbose_name="URL", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        db_table = "blog_categories"


class Product(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name="название"
    )
    descr = models.TextField(verbose_name="описание")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена товара"
    )

    is_published = models.BooleanField(
        default=True,
        verbose_name="публикация"
    )
    date_created = models.DateTimeField(
        default=now,
        verbose_name="дата создания"
    )

    date_update = models.DateTimeField(
        auto_now=True,
        verbose_name='Время изменения'
    )

    slug = models.SlugField(
        verbose_name="URL",
        unique=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        verbose_name="категория"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор',
    )

    def __str__(self):
        return self.title

    @property
    def date_created_property(self):
        return self.date_created.strftime('%d.%m.%y')

    @property
    def date_update_property(self) -> str:
        return self.date_update.strftime("%d.%m.%y, %H:%M:%S")

    class Meta:
        db_table = "mainsite_products"
        verbose_name = "изделие"
        verbose_name_plural = "изделия"
        ordering = ["date_created"]
