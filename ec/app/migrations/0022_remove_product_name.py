# Generated by Django 4.1.7 on 2023-04-29 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
    ]
