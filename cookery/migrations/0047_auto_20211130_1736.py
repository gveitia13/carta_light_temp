# Generated by Django 3.2.3 on 2021-11-30 22:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookery', '0046_categoria_usuario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ('orden',), 'verbose_name': 'Categoria', 'verbose_name_plural': '02 - Categorías'},
        ),
        migrations.AlterField(
            model_name='product',
            name='contenido',
            field=ckeditor.fields.RichTextField(verbose_name='Descripción'),
        ),
    ]