# Generated by Django 3.1.4 on 2021-02-04 05:46

import ckeditor.fields
import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre del negocio')),
                ('logo', models.ImageField(upload_to='cfg/')),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=18, verbose_name='Color principal')),
                ('color2', colorfield.fields.ColorField(default='#FF0000', max_length=18, verbose_name='Color secundario')),
                ('texto_redes', ckeditor.fields.RichTextField(help_text='Se muestra en todas las páginas', verbose_name='Texto sobre los enlaces a las redes sociales')),
                ('instagram', models.CharField(blank=True, help_text='Opcional', max_length=255, verbose_name='Enlace a Instagram')),
                ('facebook', models.CharField(blank=True, help_text='Opcional', max_length=255, verbose_name='Enlace a Facebook')),
                ('telegram', models.CharField(blank=True, help_text='Opcional', max_length=255, verbose_name='Contacto de Telegram')),
                ('whatsapp', models.CharField(blank=True, help_text='Opcional', max_length=255, verbose_name='Contacto de WhatsApp')),
            ],
            options={
                'verbose_name': 'Configuración',
                'verbose_name_plural': '1 - Configuraciones',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Resolución recomendada 1024x768', upload_to='productos/', verbose_name='Imagen')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('price', models.FloatField(blank=True, default=0, help_text='Opcional', null=True, verbose_name='Precio')),
                ('contenido', ckeditor.fields.RichTextField()),
                ('especial', models.BooleanField(default=False)),
                ('visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='SeccionCarta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('subtitulo', models.CharField(blank=True, help_text='Opcional', max_length=255, null=True, verbose_name='Subítulo')),
                ('contenido', ckeditor.fields.RichTextField(blank=True, help_text='Opcional', null=True)),
            ],
            options={
                'verbose_name': 'Sección principal',
                'verbose_name_plural': '2 - Sección principal',
            },
        ),
        migrations.CreateModel(
            name='SeccionContacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('subtitulo', models.CharField(blank=True, help_text='Opcional', max_length=255, null=True, verbose_name='Subítulo')),
                ('contenido', ckeditor.fields.RichTextField(blank=True, help_text='Opcional', null=True)),
            ],
            options={
                'verbose_name': 'Sección contacto',
                'verbose_name_plural': '4 - Sección contacto',
            },
        ),
        migrations.CreateModel(
            name='SeccionNosotros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('subtitulo', models.CharField(blank=True, help_text='Opcional', max_length=255, null=True, verbose_name='Subítulo')),
                ('contenido', ckeditor.fields.RichTextField(blank=True, help_text='Opcional', null=True)),
            ],
            options={
                'verbose_name': 'Sección nosotros',
                'verbose_name_plural': '3 - Sección nosotros',
            },
        ),
        migrations.CreateModel(
            name='SeccionNosotrosPerks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='cookery/secciones/')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('contenido', ckeditor.fields.RichTextField(blank=True, help_text='Opcional', null=True)),
            ],
            options={
                'verbose_name': 'Punto',
                'verbose_name_plural': 'Puntos',
            },
        ),
        migrations.CreateModel(
            name='SeccionPrincipal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='cookery/secciones/')),
                ('texto_sup', models.CharField(blank=True, help_text='Opcional', max_length=255, null=True, verbose_name='Texto sobre el título')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
            ],
            options={
                'verbose_name': 'Sección carta',
                'verbose_name_plural': '3 - Sección carta',
            },
        ),
        migrations.CreateModel(
            name='ProductoPerks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(max_length=255)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookery.product')),
            ],
            options={
                'verbose_name': 'Información adicional',
                'verbose_name_plural': 'Informaciones adicionales',
            },
        ),
        migrations.CreateModel(
            name='GaleriaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Resolución recomendada 1024x768', upload_to='productos/', verbose_name='Imagen')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookery.product')),
            ],
            options={
                'verbose_name': 'Imagen de productos',
                'verbose_name_plural': 'Imágenes de productos',
            },
        ),
    ]
