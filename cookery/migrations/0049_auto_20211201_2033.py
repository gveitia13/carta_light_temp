# Generated by Django 3.2.3 on 2021-12-02 01:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookery', '0048_alter_categoria_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuracion',
            name='regenerar',
        ),
        migrations.AlterField(
            model_name='product',
            name='contenido',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Descripción'),
        ),
    ]
