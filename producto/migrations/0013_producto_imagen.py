# Generated by Django 3.0.6 on 2023-07-29 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0012_auto_20230725_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
