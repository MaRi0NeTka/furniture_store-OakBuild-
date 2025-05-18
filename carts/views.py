from django.shortcuts import redirect

from carts.models import Cart
from goods.models import Products


def cart_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)#получаем QuerySet по слагу
    if request.user.is_authenticated:#проверяем авторизован ли пользователь
        cart = Cart.objects.filter(user=request.user, product=product)# получаем карточку товара в корзине пользователя
        if cart.exists(): #проверяем существует ли карточка товара в корзине, если существует, то прибавляем к ней +1
            print(list(cart))
            cart = cart.first()# получаем первый элемент из QuerySet, хоть он там и один
            print(cart)
            cart.quantity +=1
            cart.save() # сохраняем изменения в карточке товара
        else: #если карточки товара в корзине нет, то создаем новую
            cart = Cart.objects.create(user=request.user, product=product, quantity=1)
    
    return redirect(request.META['HTTP_REFERER'])# оставляем пользователя на той же странице, где он кликнул на кнопку "Добавить в корзину"


def cart_change(request, product_slug):
    ...

def cart_remove(request, product_slug):
    ...