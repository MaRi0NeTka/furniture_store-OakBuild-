from django.db import transaction
from django.forms import ValidationError
from django.contrib import messages
from django.shortcuts import redirect, render

from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


def create_order(request):
    if request.method == "POST":
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    carts_items = Cart.objects.filter(user=user)

                    if carts_items.exists():
                        # Создаем заказ
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_adress=form.cleaned_data['delivery_adress'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )

                        # Добавляем товары в заказ
                        for item in carts_items:
                            product = item.product
                            name = product.name
                            price = product.get_sell_price()
                            quantity = item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(f'Недостаточно товара {name} на складе. Доступно: {product.quantity}, запрошено: {quantity}')
                            
                            # Создаем элемент заказа
                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                quantity=quantity,
                                price=price,
                            )
                            # Уменьшаем количество товара на складе
                            product.quantity -= quantity
                            product.save()
                        # Очищаем корзину
                        carts_items.delete()
                        messages.success(request, 'Заказ успешно оформлен!')
                        return redirect('user:profile')


            except ValidationError as e:
                messages.warning(request, str(e))  
                return redirect('cart:order')
    else:
        initial_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }        
        form = CreateOrderForm(initial=initial_data)
    context = {
        'title': 'Home - Оформление заказа',
        'form': form,
    }

    return render(request, 'orders/create_order.html', context=context)