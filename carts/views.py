from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string

from carts.models import Cart
from carts.utils import get_user_carts
from goods.models import Products


def cart_add(request):
    product_id = request.POST.get('product_id')# получаем id товара из POST запроса

    product = Products.objects.get(id=product_id)#получаем QuerySet по слагу
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
    
    user_carts = get_user_carts(request)# получаем все корзины с товарами пользователя

    #передаем данные для перерисовки в шаблоне корзины
    cart_items_html = render_to_string(
        'carts/includes/include_cart.html', {'carts':user_carts}, request=request
    )

    response_data = {
        'message': 'Товар добавлен в корзину',
        'cart_items_html':cart_items_html,
    }
    return JsonResponse(response_data)


def cart_change(request, product_slug):
    ...

def cart_remove(request):
    ...
    # cart = Cart.objects.get(id=cart_id)
    # cart.delete()
    # return redirect(request.META["HTTP_REFERER"])