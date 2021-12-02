import hashlib
import os
from datetime import datetime
from pathlib import Path
from django.contrib.auth.models import User
import qrcode
from django.db import models
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
import shutil
from .get_user import current_request


#defs
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from docutils.utils.math.latex2mathml import mo


def hash_string(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

def walk_up_folder(path, depth=1):
    _cur_depth = 1
    while _cur_depth < depth:
        path = os.path.dirname(path)
        _cur_depth += 1
    return path

# Create your models here.
class ConfiguracionGodlango(models.Model):
    url = models.CharField(max_length=500)

    def __str__(self):
        return 'Configuraciones de ámbito global'

    class Meta:
        verbose_name_plural = '*  Configuraciones de ámbito global'
        verbose_name = 'Configuración de ámbito global'
        app_label = 'godjango'

class Categoria(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    categoria = models.CharField(max_length=255)
    orden = models.IntegerField()

    def __str__(self):
        return self.categoria

    class Meta:
        verbose_name_plural = '02 - Categorías'
        verbose_name = 'Categoria'
        ordering = ('orden',)

class Configuracion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    nombre = models.CharField(max_length=255, verbose_name='Nombre del negocio')
    logo = models.ImageField(upload_to='cfg/', verbose_name='Imagen principal')
    moneda = models.CharField(max_length=255, verbose_name='Moneda a usar en la plataforma', default='U.S.D')
    color = ColorField(default='#97824B', verbose_name='Color principal')
    color2 = ColorField(default='#005238', verbose_name='Color secundario')
    color3 = ColorField(default='#005238', verbose_name='Color de fondo')
    tel = models.CharField(max_length=255, verbose_name='Telefono fijo del establecimiento', help_text='Opcional', blank=True)
    direccion = models.CharField(max_length=255, verbose_name='Dirección particular', help_text='Opcional', blank=True)
    whatsapp = models.CharField(max_length=255, verbose_name='Contacto de WhatsApp', help_text='Opcional', blank=True)
    recibir_pedidos = models.BooleanField(default=True)
    qr_img = models.CharField(max_length=900)


    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="300" height="300" />' % (str(self.qr_img)))
    image_tag.short_description = 'Vista previa'

    def show_url(self):
        return mark_safe("<a href='/media/%s'>%s</a>" % (self.qr_img, str(ConfiguracionGodlango.objects.all()[0].url) + str(self.usuario.username)))
    show_url.short_description = 'Url'

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.qr_img :
            user = self.usuario
            qr = qrcode.make()
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=50,
                border=4,
            )
            qr.add_data(str(ConfiguracionGodlango.objects.all()[0].url +  str(user.username)))
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
            self.qr_img = "/qr/" + str(self.pk) + '.png'
            # qr.save("media/qr/" + str(self.id) + '.png')
            img.save("media/qr/" + str(self.pk) + '.png')
            self.regenerar = False
        super(Configuracion, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = '01 - Configuraciones'
        verbose_name = 'Configuración'

class Product(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    cfg = models.ForeignKey(Configuracion, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='productos/', verbose_name='Imagen', help_text='Resolución recomendada 400x300')
    name = models.CharField(max_length=255, verbose_name='Nombre')
    price = models.FloatField(default=0, verbose_name='Precio', help_text='Opcional')
    contenido = RichTextField(verbose_name='Descripción', null=True, blank=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super(Product, self).__init__(*args, **kwargs)
        self.__precio = self.price

    def resumen(self):
        if len(self.contenido) > 60:
            return self.contenido[:57] + ' ...'
        return self.contenido

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="120" height="120" />' % (str(self.image)))

    image_tag.short_description = 'Vista previa'

    class Meta:
        verbose_name_plural = 'Productos'
        verbose_name = 'Producto'

class Zona(models.Model):
    cfg = models.ForeignKey(Configuracion, on_delete=models.CASCADE)
    dia = models.CharField(max_length=255)
    horario = models.CharField(max_length=255)

    def __str__(self):
        return 'Especificaciones del servicio a domicilio'

    class Meta:
        verbose_name = 'Especificaciones del servicio a domicilio'
        verbose_name_plural = 'Especificaciones del servicio a domicilio'
