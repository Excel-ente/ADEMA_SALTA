# Generated by Django 3.0.6 on 2023-07-25 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0008_compra_viaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fecha',
            field=models.DateField(),
        ),
    ]