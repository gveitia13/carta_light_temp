# Generated by Django 3.2.3 on 2021-11-26 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('godjango', '0016_auto_20211125_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despliegue',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2021, 11, 26, 6, 42, 59, 203850)),
        ),
    ]