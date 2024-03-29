# Generated by Django 5.0.1 on 2024-01-12 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('category', models.CharField(choices=[('meat', 'meat'), ('fast food', 'fast food'), ('vegetables', 'vegetables')], default='vegetables', max_length=20)),
                ('img', models.ImageField(upload_to='media/product/%y/%m/%d')),
                ('slug', models.SlugField(max_length=200)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
