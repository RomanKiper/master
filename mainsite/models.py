from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class TypeOfPublications(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name="вид публикации",
        help_text="выберите вид публикации"
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="опубликовать"
    )
    slug = models.SlugField(verbose_name="URL", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "вид публикации"
        verbose_name_plural = "вид публикций"
        db_table = "type_of_publications"


class Publication(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name="название"
    )
    descr = models.TextField(verbose_name="описание")
    is_published = models.BooleanField(
        default=False,
        verbose_name="публикация"
    )
    date_created = models.DateTimeField(
        default=now,
        verbose_name="дата создания"
    )
    slug = models.SlugField(
        verbose_name="URL",
        unique=True
    )
    type_of_publication = models.ForeignKey(
        TypeOfPublications,
        on_delete=models.DO_NOTHING,
        verbose_name="вид публикации"
    )
    image = models.ImageField(
        upload_to='post',
        verbose_name='картинка',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("mainsite_publication", kwargs={"publication_slug": self.slug})

    class Meta:
        db_table = "mainsite_publication"
        verbose_name = "публикация"
        verbose_name_plural = "публикации"
        ordering = ["date_created"]



class FilterPrice(models.Model):
    name = models.CharField(
        max_length=64,
        null=True,
        verbose_name="диапазон цены",
        help_text="Выберите в какой диапазон входит цена товара"
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name="активировать"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "диапазон цены"
        verbose_name_plural = "диапазон цен"
        db_table = "filter_price"


class FilterAvailability(models.Model):
    name = models.CharField(
        max_length=64,
        null=True,
        verbose_name="наличие на складе",
        help_text="Укажите есть товар в наличии или он под заказ"
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name="наличие на складе"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "наличие товара"
        verbose_name_plural = "наличие товаров"
        db_table = "filter_availability"


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
    image = models.ImageField(
        upload_to='post',
        verbose_name='картинка',
        null=True,
        blank=True
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

    # товар-новинка
    novelty = models.BooleanField(
        default=False,
        verbose_name="новый товар"
    )

    # популярность товара
    popularity = models.BooleanField(
        default=False,
        verbose_name="популярный товар",
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
    filter_availability = models.ForeignKey(
        FilterAvailability,
        on_delete=models.DO_NOTHING,
        verbose_name="наличие товара",
        default=True
    )
    filter_price = models.ForeignKey(
        FilterPrice,
        on_delete=models.DO_NOTHING,
        verbose_name="диапазон цены",
        default = True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор',
    )
    image = models.ImageField(
        upload_to='post',
        verbose_name='картинка',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("mainsite_product", kwargs={"product_slug": self.slug})

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


class Contact(models.Model):
    name = models.CharField(max_length=64, verbose_name="имя")
    email= models.EmailField(verbose_name='почта')
    message = models.CharField(max_length=1024, verbose_name='сообщение')
    phone = models.CharField(max_length=64, verbose_name='номер телефона')
    date_created = models.DateTimeField(default=now, verbose_name="дата обращения")
    is_published = models.BooleanField(default=False,verbose_name="прочитано",)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'mainsite_contacts'
        verbose_name = "контакт"
        verbose_name_plural = "База контактов"
        ordering = ['date_created',]


class EmailBase(models.Model):
    email = models.CharField(max_length=64, verbose_name='эллектронная почта')
    date_created = models.DateTimeField(default=now, verbose_name="дата контакта")
    is_published = models.BooleanField(default=False, verbose_name="прочитано",)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'mainsite_email_base'
        verbose_name = "адрес почты"
        verbose_name_plural = "база эллектронных адресов"
        ordering = ['date_created',]



