# Generated by Django 4.1.4 on 2022-12-21 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainsite", "0005_contact_is_published"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="post", verbose_name="картинка"
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="is_published",
            field=models.BooleanField(default=False, verbose_name="прочитано"),
        ),
    ]
