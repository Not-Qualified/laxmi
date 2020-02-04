# Generated by Django 3.0.2 on 2020-02-03 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_type', models.CharField(choices=[('G', 'Gold'), ('S', 'Silver'), ('O', 'Other')], max_length=1)),
                ('product_weight', models.DecimalField(decimal_places=3, max_digits=21)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.ProductCategory')),
            ],
        ),
    ]
