# Generated by Django 3.2.3 on 2021-11-26 01:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('godjango', '0015_alter_despliegue_hora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuraciongodlango',
            name='porciento',
        ),
        migrations.AlterField(
            model_name='despliegue',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2021, 11, 25, 20, 54, 48, 738097)),
        ),
    ]