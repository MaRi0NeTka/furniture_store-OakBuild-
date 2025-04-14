from django.shortcuts import render
from goods.models import Products

def catalog(request):
    goods = Products.objects.all() #получаем все товары из базы данных
    context = {
        'title': 'House - Каталог товаров',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context=context)


def product(request, product_slug=False, product_id=False):
    if product_id: #если передан id товара
        product = Products.objects.get(id = product_id) #получаем товар по id
    else:    
        product = Products.objects.get(slug = product_slug) #получаем товар по slug
    context = {
        'product': product,
    }
    return render(request, 'goods/product.html', context=context)