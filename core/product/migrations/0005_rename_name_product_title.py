# Generated by Django 4.1 on 2023-10-22 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_product', '0004_alter_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='title',
        ),
    ]