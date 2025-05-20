from django import template

from carts.utils import get_user_carts

register = template.Library()

@register.simple_tag()
def user_carts(request):
    # Получаем все корзины пользователя
    # Чтобы они были доступны в шаблоне
    return get_user_carts(request)