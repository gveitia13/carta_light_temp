# Generated by Django 3.1.4 on 2021-02-22 05:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('godjango', '0007_auto_20210222_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despliegue',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2021, 2, 22, 0, 31, 52, 190512)),
        ),
    ]
