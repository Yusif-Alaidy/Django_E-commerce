# Generated by Django 4.2.7 on 2024-02-12 06:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_remove_review_revproduct_review_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 12, 8, 15, 48, 468421)),
        ),
    ]