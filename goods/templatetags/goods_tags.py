from django import template
from goods.models import Categories

register = template.Library()#регистрируем библиотеку шаблонов

@register.simple_tag()
def get_categories():
    return Categories.objects.all()#выбираем все объекты из базы данных