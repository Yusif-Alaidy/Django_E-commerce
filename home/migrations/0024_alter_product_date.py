# Generated by Django 4.2.7 on 2024-02-12 23:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_product_date_alter_review_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 13, 1, 7, 41, 217563)),
        ),
    ]