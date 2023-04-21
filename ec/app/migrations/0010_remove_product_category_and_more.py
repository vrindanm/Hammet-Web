# Generated by Django 4.1.7 on 2023-04-06 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='discounted_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='selling_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('stock', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
    ]
