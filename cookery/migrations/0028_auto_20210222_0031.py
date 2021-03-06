# Generated by Django 3.1.4 on 2021-02-22 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cookery', '0027_zona'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zona',
            options={'verbose_name': 'Especificaciones del servicio a domicilio', 'verbose_name_plural': '11 - Especificaciones del servicio a domicilio'},
        ),
        migrations.RemoveField(
            model_name='zona',
            name='precio',
        ),
        migrations.RemoveField(
            model_name='zona',
            name='zona',
        ),
        migrations.CreateModel(
            name='ZonaPerk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zona', models.CharField(max_length=255)),
                ('precio', models.CharField(max_length=255, verbose_name='Precio')),
                ('fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookery.zona')),
            ],
            options={
                'verbose_name': 'Zona',
                'verbose_name_plural': 'Zonas',
            },
        ),
    ]
