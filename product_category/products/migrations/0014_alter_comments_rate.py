# Generated by Django 4.0.3 on 2022-04-20 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_comments_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='rate',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True),
        ),
    ]
