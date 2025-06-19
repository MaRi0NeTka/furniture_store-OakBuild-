from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.views import View

from carts.custom_mixin import CartMixin
from carts.models import Cart
from carts.utils import get_user_carts
from goods.models import Products



class CartAddView(CartMixin, View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        product = Products.objects.get(id = product_id)
        carts = self.get_carts(request, product=product)# получаем корзину пользователя по продукту
        if carts:# проверяем существует ли корзина с данным продуктом и добавляем +1 к количеству
            carts.quantity += 1
            carts.save()
        else: # если корзины с данным продуктом нет, то создаем новую корзину
            carts = Cart.objects.create(user=request.user if request.user.is_authenticated else None,
                                            session_key = request.session.session_key if not request.user.is_authenticated else None,
                                            product=product,
                                            quantity=1)

        response_data = {                   # формируем ответ для AJAX запроса           
            'message': 'Товар добавлен в корзину',
            'cart_items_html': self.render_cart_items(request),
        }
        return JsonResponse(response_data)
    

class CartChangeView(CartMixin, View):
    def post(self, request):
        cart_id = request.POST.get('cart_id')
        cart = self.get_carts(request, cart_id=cart_id)

        cart.quantity = request.POST.get('quantity')
        cart.save()  # сохраняем изменения в количестве товара
        quantity = cart.quantity

        response_data = {
            'message': 'Количество товара изменено',
            'cart_items_html': self.render_cart_items(request),
            'quantity': quantity
        }
        return JsonResponse(response_data)
    
class CartRemoveView(CartMixin, View):
    def post(self, request):
        cart_id = request.POST.get('cart_id')
        cart = self.get_carts(request, cart_id=cart_id)
        quantity= cart.quantity
        cart.delete()  # удаляем товар из корзины

        response_data = {
            'message': 'Товар удален из корзины',
            'cart_items_html': self.render_cart_items(request),
            'quantity_deleted': quantity,
        }
        return JsonResponse(response_data)

# def cart_add(request):
#     product_id = request.POST.get('product_id')# получаем id товара из POST запроса

#     product = Products.objects.get(id=product_id)#получаем QuerySet по слагу
#     if request.user.is_authenticated:#проверяем авторизован ли пользователь
#         cart = Cart.objects.filter(user=request.user, product=product)# получаем карточку товара в корзине пользователя
#         if cart.exists(): #проверяем существует ли карточка товара в корзине, если существует, то прибавляем к ней +1
#             cart = cart.first()# получаем первый элемент из QuerySet, хоть он там и один
#             cart.quantity +=1
#             cart.save() # сохраняем изменения в карточке товара
#         else: #если карточки товара в корзине нет, то создаем новую
#             cart = Cart.objects.create(user=request.user, product=product, quantity=1)
#     else:# если пользователь не авторизован, то создаем корзину по session_key
#         #привязываем корзину к сессионному ключу пользователя
#         cart = Cart.objects.filter(session_key=request.session.session_key, product=product)
#         if cart.exists():
#             cart = cart.first()
#             cart.quantity += 1
#             cart.save()
#         else:
#             # создаем новую корзину для неавторизованного пользователя по сессионному ключу
#             cart = Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)

    
#     user_carts = get_user_carts(request)# получаем все корзины с товарами пользователя

#     #передаем данные для перерисовки в шаблоне корзины
#     cart_items_html = render_to_string(
#         'carts/includes/include_cart.html', {'carts':user_carts}, request=request
#     )

#     response_data = {
#         'message': 'Товар добавлен в корзину',
#         'cart_items_html':cart_items_html,
#     }
#     return JsonResponse(response_data)


# def cart_change(request):
#     cart_id = request.POST.get('cart_id')
#     quantity = request.POST.get('quantity')
#     cart = Cart.objects.get(id=cart_id)
#     cart.quantity = quantity
#     cart.save()

#     user_carts = get_user_carts(request)
#     cart_items_html = render_to_string(
#         'carts/includes/include_cart.html', {'carts':user_carts}, request=request
#     )
#     response_data = {
#         'message': 'Количество товара изменено',
#         'cart_items_html': cart_items_html,
#         'quantity': quantity
#     }
#     return JsonResponse(response_data)

# def cart_remove(request):
#     cart_id = request.POST.get('cart_id')# получаем id карточки товара из POST запроса

#     cart = Cart.objects.get(id=cart_id)
#     quantity = cart.quantity
#     cart.delete()
    
#     user_carts = get_user_carts(request)# получаем все корзины с товарами пользователя
#     cart_items_html = render_to_string(
#         'carts/includes/include_cart.html', {'carts':user_carts}, request=request
#     )

#     response_data = {
#         'message': 'Товар удален из корзины',
#         'cart_items_html': cart_items_html,
#         'quantity_deleted': quantity,
#     }
#     return JsonResponse(response_data)