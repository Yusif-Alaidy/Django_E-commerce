# Generated by Django 4.2.7 on 2024-01-28 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(default='default.png', upload_to='product/years=%y/month=%m'),
        ),
    ]
