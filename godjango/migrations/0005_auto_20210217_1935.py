# Generated by Django 3.1.4 on 2021-02-18 00:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('godjango', '0004_auto_20210217_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despliegue',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2021, 2, 17, 19, 35, 17, 842997)),
        ),
    ]
