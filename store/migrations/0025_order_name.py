# Generated by Django 3.1.2 on 2020-12-09 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_delete_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
