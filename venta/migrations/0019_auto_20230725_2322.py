# Generated by Django 3.0.6 on 2023-07-26 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0018_venta_vendedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]