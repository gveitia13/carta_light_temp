# Generated by Django 3.2.3 on 2021-11-30 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookery', '0042_auto_20211130_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='recibir_pedidos',
            field=models.BooleanField(default=True),
        ),
    ]