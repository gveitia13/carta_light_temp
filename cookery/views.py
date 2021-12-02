from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaulttags import register

from .models import *
from django.core.mail import EmailMessage
from django.utils.safestring import mark_safe
from carta.settings import CART_SESSION_ID, CARRITO_SESSION_ID
from cart.cart import Cart
from .forms import *
from datetime import datetime, timedelta
from pytz import timezone
import pytz
from django.http.response import JsonResponse
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    inicio = True
    if not request.session.get(CART_SESSION_ID):
        request.session[CART_SESSION_ID] = {}
    total = 0
    for value in request.session[CART_SESSION_ID]:
        total = total + float(request.session[CART_SESSION_ID][value]['price']) * float(
            request.session[CART_SESSION_ID][value]['quantity'])
    cfg = Configuracion.objects.all()[0]
    principal = SeccionPrincipal.objects.all()[0]
    nosotros = SeccionNosotros.objects.all()[0]
    menu = SeccionCarta.objects.all()[0]
    especiales = Product.objects.all().filter(especial=True).filter(visible=True)
    return render(request, 'index.html', {'total':total, 'cfg':cfg, 'principal':principal, 'nosotros':nosotros, 'especiales':especiales, 'menu':menu})

def index2(request):
    if not request.session.get(CART_SESSION_ID):
        request.session[CART_SESSION_ID] = {}
    total = 0
    for value in request.session[CART_SESSION_ID]:
        total = total + float(request.session[CART_SESSION_ID][value]['price']) * float(
            request.session[CART_SESSION_ID][value]['quantity'])
    cfg = Configuracion.objects.all()[0]
    principal = SeccionPrincipal.objects.all()[0]
    nosotros = SeccionNosotros.objects.all()[0]
    menu = SeccionCarta.objects.all()[0]
    especiales = Product.objects.all().filter(especial=True).filter(visible=True)
    return render(request, 'index2.html', {'total':total, 'cfg':cfg, 'principal':principal, 'nosotros':nosotros, 'especiales':especiales, 'menu':menu})


def carta(request):
    if not request.session.get(CART_SESSION_ID):
        request.session[CART_SESSION_ID] = {}
    total = 0
    for value in request.session[CART_SESSION_ID]:
        total = total + float(request.session[CART_SESSION_ID][value]['price']) * float(
            request.session[CART_SESSION_ID][value]['quantity'])
    cfg = Configuracion.objects.all()[0]
    especiales = Product.objects.all().filter(especial=True).filter(visible=True)
    carta = SeccionCarta.objects.all()[0]
    productos = Product.objects.all().filter(visible=True)
    return render(request, 'menu.html', {'total':total, 'cfg':cfg, 'especiales':especiales, 'carta':carta, 'productos':productos})

def contacto(request):
    if not request.session.get(CART_SESSION_ID):
        request.session[CART_SESSION_ID] = {}
    total = 0
    for value in request.session[CART_SESSION_ID]:
        total = total + float(request.session[CART_SESSION_ID][value]['price']) * float(
            request.session[CART_SESSION_ID][value]['quantity'])
    cfg = Configuracion.objects.all()[0]
    especiales = Product.objects.all().filter(especial=True).filter(visible=True)
    contacto = SeccionContacto.objects.all()[0]
    form = ReservacionForm()
    if request.method == 'POST':
        form = ReservacionForm(request.POST)
        if form.is_valid():
            aux = []
            for destinatario in Destinatario.objects.all():
                aux.append(destinatario.email)
            if len(aux) == 0:
                aux.append('lmdelbahia@gmail.com')
            mensaje = 'Contacto: ' + mark_safe('<br/>')
            mensaje = mensaje + 'Nombre: ' + form.cleaned_data['nombre'] + mark_safe('<br/>')
            mensaje = mensaje + 'Teléfono: ' + form.cleaned_data['telefono'] + mark_safe('<br/>')
            mensaje = mensaje + form.cleaned_data['asunto'] + mark_safe('<br/>')
            mensaje = mensaje + form.cleaned_data['mensaje']
            email = EmailMessage(subject='Contacto',body=mensaje,from_email=form.cleaned_data['telefono'],to=aux,bcc=None,connection=None
                                 ,attachments=None, headers=None, cc=None, reply_to=None)
            email.content_subtype = 'html'
            email.send()
            contacto = Reservacion()
            contacto.nombre = form.cleaned_data['nombre']
            contacto.asunto = form.cleaned_data['asunto']
            contacto.telefono = form.cleaned_data['telefono']
            contacto.mensaje = form.cleaned_data['mensaje']
            contacto.save()
            return redirect('/')
        else:
            form = ReservacionForm(request.POST)
    return render(request, 'contact.html', {'total':total, 'cfg':cfg, 'especiales':especiales, 'contacto':contacto, 'form':form})

def producto_detail(request, producto_id):
    if not request.session.get(CART_SESSION_ID):
        request.session[CART_SESSION_ID] = {}
    total = 0
    for value in request.session[CART_SESSION_ID]:
        total = total + float(request.session[CART_SESSION_ID][value]['price']) * float(
            request.session[CART_SESSION_ID][value]['quantity'])
    cfg = Configuracion.objects.all()[0]
    especiales = Product.objects.all().filter(especial=True).filter(visible=True)
    carta = SeccionCarta.objects.all()[0]
    productos = Product.objects.all().filter(visible=True)
    producto = productos.get(pk=producto_id)
    comentarios = producto.comentario_set.all().filter(valido=True)
    flag = False
    if producto.comentario_set.filter(valido=True):
        flag = True
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.product = producto
            comentario.fecha = datetime.now()
            comentario.save()
            return redirect('producto_detail', producto_id=producto.id)
    else:
        form = ComentarioForm()
    return render(request, 'single.html', {'total':total, 'cfg':cfg, 'especiales':especiales, 'carta':carta, 'productos':productos, 'producto':producto, 'form':form, 'comentarios':comentarios, 'flag':flag})

def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("carta")

def cart_add_ajax(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return JsonResponse({'name':product.name, 'id':product.id, 'price':product.price}, safe=False)

def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

def item_clear_ajax(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    quantity = request.session[CART_SESSION_ID][str(product.id)]['quantity']
    total = 0
    for value in request.session[CART_SESSION_ID]:
        total = total + float(request.session[CART_SESSION_ID][value]['price']) * float(
            request.session[CART_SESSION_ID][value]['quantity'])
    cart.remove(product)
    return JsonResponse({'name':product.name, 'id':product.id, 'price':product.price, 'quantity':quantity}, safe=False)


def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")

def cart_decrement_ajax(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return JsonResponse({'name':product.name, 'id':product.id, 'price':product.price}, safe=False)


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")

def cart_clear_ajax(request):
    cart = Cart(request)
    cart.clear()
    return JsonResponse({'status':"OK"}, safe=False)

def cart_detail(request, username):
    usuario = get_object_or_404(User, username=username)
    if not request.session.get(CART_SESSION_ID):
        request.session[CART_SESSION_ID] = {}
    zonas = Zona.objects.all()[0]
    total = 0
    cfg = Configuracion.objects.all().get(usuario=usuario)
    categorias = Categoria.objects.all().filter(usuario=cfg.usuario)
    productos = Product.objects.all().filter(visible=True, cfg=cfg).order_by('categoria__orden')
    for value in request.session[CART_SESSION_ID]:
        total = total + float(request.session[CART_SESSION_ID][value]['price'])*float(request.session[CART_SESSION_ID][value]['quantity'])
    cantidades = {}
    for producto in productos:
        if str(producto.pk) in request.session[CART_SESSION_ID]:
            cantidades[producto.pk] = request.session[CART_SESSION_ID][str(producto.pk)]['quantity']
        else:
            cantidades[producto.pk] = 0

    if request.method == 'POST':
        json_msg = ""
    return render(request, 'cart_detail.html',{'cfg':cfg,'total':total, 'carta':carta, 'zonas':zonas,'productos':productos,
                                               'cantidades':cantidades, 'categorias':categorias})

def cart_load(request):
    total = 0
    for value in request.session[CART_SESSION_ID]:
        total = total + float(request.session[CART_SESSION_ID][value]['price'])*float(request.session[CART_SESSION_ID][value]['quantity'])

def enrutar(request, username):
    usuario = get_object_or_404(User, username=username)
    cfg = Configuracion.objects.get(usuario=usuario)
    if not request.session.get(CART_SESSION_ID):
        request.session[CART_SESSION_ID] = {}
    total = 0
    for value in request.session[CART_SESSION_ID]:
        total = total + float(request.session[CART_SESSION_ID][value]['price'])*float(request.session[CART_SESSION_ID][value]['quantity'])
    mensaje = ''
    for value in request.session[CART_SESSION_ID]:
        precio = request.session[CART_SESSION_ID][value]['quantity'] * float(
            request.session[CART_SESSION_ID][value]['price'])
        mensaje = mensaje + '• ' + str(request.session[CART_SESSION_ID][value]['quantity']) + 'x ' + \
                  request.session[CART_SESSION_ID][value]['name'] + ': $' + str(precio) + mark_safe(' <br/> ')
    mensaje = mensaje + 'Total: ' + str(total)
    return redirect('https://api.whatsapp.com/send?phone='+str(cfg.whatsapp)+'&text='+mensaje)

def vacio(request):
    return render(request, 'contact.html')
