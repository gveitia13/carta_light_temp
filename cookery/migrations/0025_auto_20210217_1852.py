# Generated by Django 3.1.4 on 2021-02-17 23:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookery', '0024_auto_20210217_1644'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'verbose_name': 'Comentario', 'verbose_name_plural': '09 - Comentarios'},
        ),
        migrations.AlterModelOptions(
            name='configuracion',
            options={'verbose_name': 'Configuración', 'verbose_name_plural': '01 - Configuraciones'},
        ),
        migrations.AlterModelOptions(
            name='destinatario',
            options={'verbose_name': 'Destinatario', 'verbose_name_plural': '08 - Destinatarios'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Producto', 'verbose_name_plural': '06 - Productos'},
        ),
        migrations.AlterModelOptions(
            name='reservacion',
            options={'verbose_name': 'Contacto', 'verbose_name_plural': '07 - Contactos'},
        ),
        migrations.AlterModelOptions(
            name='seccioncarta',
            options={'verbose_name': 'Sección carta', 'verbose_name_plural': '03 - Sección carta'},
        ),
        migrations.AlterModelOptions(
            name='seccioncontacto',
            options={'verbose_name': 'Sección contacto', 'verbose_name_plural': '05 - Sección contacto'},
        ),
        migrations.AlterModelOptions(
            name='seccionnosotros',
            options={'verbose_name': 'Sección nosotros', 'verbose_name_plural': '04 - Sección nosotros'},
        ),
        migrations.AlterModelOptions(
            name='seccionprincipal',
            options={'verbose_name': 'Sección principal', 'verbose_name_plural': '02 - Sección principal'},
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 17, 18, 52, 31, 950839), editable=False),
        ),
    ]
