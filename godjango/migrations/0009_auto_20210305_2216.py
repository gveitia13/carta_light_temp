# Generated by Django 3.1.7 on 2021-03-06 03:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('godjango', '0008_auto_20210222_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despliegue',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2021, 3, 5, 22, 16, 38, 279060)),
        ),
    ]
