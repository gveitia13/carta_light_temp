# Generated by Django 3.1.4 on 2021-02-18 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookery', '0025_auto_20210217_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='fecha',
        ),
    ]
