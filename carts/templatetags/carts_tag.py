from django import template

from carts.models import Cart

register = template.Library()

@register.simple_tag()
def user_carts(request):
    # Получаем все корзины пользователя
    # Чтобы они были доступны в шаблоне
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)