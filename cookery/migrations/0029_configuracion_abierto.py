# Generated by Django 3.1.7 on 2021-03-06 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookery', '0028_auto_20210222_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='abierto',
            field=models.BooleanField(default=True, verbose_name='Aceptar pedidos'),
        ),
    ]
