# Generated by Django 4.1 on 2023-10-22 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_product', '0002_alter_product_price_alter_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
