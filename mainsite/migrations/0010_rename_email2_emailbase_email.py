# Generated by Django 4.1.4 on 2023-01-24 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainsite", "0009_alter_contact_options_rename_email_emailbase_email2"),
    ]

    operations = [
        migrations.RenameField(
            model_name="emailbase",
            old_name="email2",
            new_name="email",
        ),
    ]
