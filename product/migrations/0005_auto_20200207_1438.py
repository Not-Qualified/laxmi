# Generated by Django 3.0.3 on 2020-02-07 09:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200207_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='product_category',
            field=models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(regex='^[A-Za-z0-9\\-\\ ]$'), django.core.validators.MinLengthValidator(limit_value=3), django.core.validators.MaxLengthValidator(limit_value=50)]),
        ),
    ]
