# Generated by Django 3.1.4 on 2021-02-09 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookery', '0019_auto_20210208_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seccioncarta',
            name='subtitulo',
        ),
    ]