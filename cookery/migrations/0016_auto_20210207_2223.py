# Generated by Django 3.1.4 on 2021-02-08 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookery', '0015_auto_20210206_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255, verbose_name='Teléfono')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': '10 - Pedidos',
            },
        ),
        migrations.AlterField(
            model_name='seccioncontactoperks',
            name='tipo',
            field=models.CharField(choices=[('tel', 'Teléfono'), ('mail', 'Email'), ('dir', 'Dirección'), ('whatsapp', 'WhatsApp'), ('hora', 'Horario')], max_length=255, verbose_name='Tipo'),
        ),
    ]
