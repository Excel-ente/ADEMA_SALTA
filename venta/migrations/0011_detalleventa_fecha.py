# Generated by Django 3.0.6 on 2023-07-23 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0010_auto_20200525_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleventa',
            name='fecha',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
