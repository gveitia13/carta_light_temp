# Generated by Django 3.2.3 on 2021-11-30 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cookery', '0045_auto_20211130_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='usuario',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
