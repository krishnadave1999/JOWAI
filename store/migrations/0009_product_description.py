# Generated by Django 3.1.2 on 2020-11-27 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_myorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=2550),
        ),
    ]
