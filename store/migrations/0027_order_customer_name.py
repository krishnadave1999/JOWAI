# Generated by Django 3.1.2 on 2020-12-09 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_remove_order_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_name',
            field=models.CharField(default='blank', max_length=200),
        ),
    ]
