# Generated by Django 4.1 on 2023-01-06 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_alter_customer_customer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_image',
            field=models.ImageField(upload_to='customer/'),
        ),
    ]
