# Generated by Django 3.0.6 on 2023-07-23 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0013_venta_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleventa',
            name='cantidad',
            field=models.DecimalField(decimal_places=2, max_digits=4, max_length=25),
        ),
    ]
