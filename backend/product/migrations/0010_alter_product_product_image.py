# Generated by Django 4.1 on 2022-10-16 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]
