# Generated by Django 3.1.1 on 2021-02-05 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0044_order_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]