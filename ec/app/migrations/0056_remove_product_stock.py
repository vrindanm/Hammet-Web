# Generated by Django 4.1.7 on 2023-06-27 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0055_size_stock_alter_cart_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
    ]