from django import template
from django.utils.http import urlencode

from goods.models import Categories

register = template.Library()#регистрируем библиотеку шаблонов

@register.simple_tag()
def get_categories():# использовал в  base.html для получения всех категорий
    return Categories.objects.all()#выбираем все объекты из базы данных

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()#получаем параметры из запроса
    query.update(kwargs) #обновляем параметры запроса новыми параметрами
    return urlencode(query)