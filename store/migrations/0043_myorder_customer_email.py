# Generated by Django 3.1.2 on 2020-12-23 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0042_myorder_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='myorder',
            name='customer_email',
            field=models.CharField(default='None', max_length=200),
        ),
    ]
