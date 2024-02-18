# Generated by Django 4.2.7 on 2024-02-12 06:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 12, 8, 18, 1, 231802)),
        ),
        migrations.AlterField(
            model_name='review',
            name='Product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.product'),
        ),
    ]