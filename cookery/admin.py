from django.contrib import admin, messages
from .forms import *
from .models import *


# Register your models here.
# inlines
class ProductoInline(admin.StackedInline):
    model = Product
    form = ProductoForm
    fieldsets = [
        ('Datos del producto', {
            # 'classes':('collapse',),
            'fields': (('image_tag', 'image'), 'categoria', 'name', 'price', 'visible', 'contenido')
        }),
    ]
    readonly_fields = ('image_tag',)
    extra = 0


class HorarioInline(admin.StackedInline):
    model = Zona
    extra = 0


# model admins

class ConfiguracionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos del producto', {
            # 'classes':('collapse',),
            'fields': ('usuario', 'nombre', 'logo', 'moneda', ('color', 'color2', 'color3'), ('image_tag', 'show_url'),
                       'tel', 'direccion', 'whatsapp', 'recibir_pedidos')
        }),
    ]
    readonly_fields = ('image_tag', 'show_url')
    inlines = [HorarioInline, ProductoInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario=request.user) \

    def get_readonly_fields(self, request, obj=None):
        fields = list(super().get_readonly_fields(request))
        if not request.user.is_superuser:
            fields.append('usuario')
        return fields


class CategoriaAdmin(admin.ModelAdmin):
    fields = [
        'categoria',
        'orden',
    ]

    def save_model(self, request, obj, form, change):
        usuario = request.user
        obj.usuario = usuario
        obj.save()
        super(CategoriaAdmin, self).save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        fields = list(super().get_readonly_fields(request))
        if not request.user.is_superuser:
            fields.append('usuario')
        return fields

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario=request.user)


# admin site register
admin.site.register(ConfiguracionGodlango)
admin.site.register(Configuracion, ConfiguracionAdmin)
admin.site.register(Categoria, CategoriaAdmin)
