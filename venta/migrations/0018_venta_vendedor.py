# Generated by Django 3.0.6 on 2023-07-25 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_vendedor'),
        ('venta', '0017_auto_20230723_0302'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='vendedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='agenda.Vendedor'),
        ),
    ]