# Generated by Django 3.0.6 on 2023-07-26 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0010_auto_20230725_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='costo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25),
            preserve_default=False,
        ),
    ]
