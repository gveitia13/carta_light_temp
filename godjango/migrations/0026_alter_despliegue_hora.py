# Generated by Django 3.2.3 on 2021-11-30 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('godjango', '0025_alter_despliegue_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despliegue',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2021, 11, 30, 7, 46, 49, 525475)),
        ),
    ]