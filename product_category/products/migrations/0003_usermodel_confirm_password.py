# Generated by Django 4.0.3 on 2022-04-13 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='confirm_password',
            field=models.CharField(default='', max_length=70),
        ),
    ]
