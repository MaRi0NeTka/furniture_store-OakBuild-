from django.shortcuts import render, get_list_or_404, redirect
from django.core.paginator import Paginator

from goods.models import Products

def catalog(request, category_slug):
    page:str = request.GET.get('page', 1) #получаем номер страницы из запроса, по умолчанию 1
    on_sale = request.GET.get('on_sale', False) #получаем параметр on_sale из запроса, по умолчанию False
    order_by_prods = request.GET.get('order_by', False) #получаем параметр order_by из запроса, по умолчанию False


    if category_slug == 'all':
        goods = Products.objects.all() #получаем все товары из базы данных
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug = category_slug)) #получаем товары по slug категории
        # if not goods.exists(): #если товаров нет, то переадресуем на ютуб или другой сайт, по желанию
        #    return redirect('https://www.youtube.com/')
    
    if on_sale: #если передан параметр on_sale, то фильтруем товары по скидке
        goods = goods.filter(discount__gt = 0) #фильтруем товары по скидке, больше 0

    if order_by_prods and order_by_prods != 'default': #если передан параметр order_by, то сортируем товары по цене
        goods = goods.order_by(order_by_prods) #сортируем товары по цене, по возрастанию или убыванию

    pagin = Paginator(goods, 3)#создание пагинации, по дефолту 3 объекта на странице
    
    #получаем номер страницы из запроса, если номер страницы больше чем количество страниц, то переходим на последнюю страницу
    current_page = pagin.page(int(page)) if int(page)<=pagin.num_pages else pagin.page(pagin.num_pages)

    context = {
        'title': 'House - Каталог товаров',
        'goods': current_page, #список товаров на текущей странице
        'category_slug': category_slug, #slug категории
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