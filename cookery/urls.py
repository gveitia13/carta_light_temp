from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from cookery.views import *

urlpatterns = [
    path('', vacio, name='vacio'),
    path('<username>/', cart_detail, name='index'),
    path('<username>/contacto/', enrutar, name='enrutar'),
    # path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/add/<int:id>/', cart_add_ajax, name='cart_add'),
    # path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_clear/<int:id>/', item_clear_ajax, name='item_clear'),
    path('cart/item_increment/<int:id>/', item_increment, name='item_increment'),
    # path('cart/item_decrement/<int:id>/', item_decrement, name='item_decrement'),
    path('cart/decrement/<int:id>/', cart_decrement_ajax, name='item_decrement'),
    path('cart/cart_clear/<username>', cart_clear, name='cart_clear'),
    #path('cuenta/', cart_detail, name='cart_detail'),

]