# Generated by Django 3.1.4 on 2021-02-06 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookery', '0008_seccioncontactoperks_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seccioncontactoperks',
            name='nombre',
            field=models.CharField(blank=True, help_text='Opcional', max_length=255, null=True, verbose_name='Nombre'),
        ),
    ]