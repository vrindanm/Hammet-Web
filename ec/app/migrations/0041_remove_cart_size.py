# Generated by Django 4.1.7 on 2023-06-01 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_size_product_sizes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='size',
        ),
    ]