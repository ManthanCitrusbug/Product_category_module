# Generated by Django 4.0.3 on 2022-04-20 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_comments_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='rate',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
    ]
