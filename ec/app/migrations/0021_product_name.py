# Generated by Django 4.1.7 on 2023-04-29 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_remove_product_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
