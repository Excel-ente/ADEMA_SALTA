# Generated by Django 3.0.6 on 2023-07-25 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_vendedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendedor',
            name='codigo',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
