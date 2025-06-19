from email.mime import base
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.http import Http404


from goods.models import Products
from goods.utils import q_search

class CatalogView(ListView):
    model = Products
    template_name = 'goods/catalog.html'
    context_object_name = 'goods' # имя переменной которая будет содержать список товаров в шаблоне
    paginate_by = 3 # количество товаров на странице
    allow_empty = False


    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        on_sale = self.request.GET.get('on_sale')
        order_by_prods = self.request.GET.get('order_by')
        query = self.request.GET.get('q', None)

        base_queryset = super().get_queryset()

        if query is not None:
            query = query.strip()
            if query == '':
                goods = base_queryset
                self.request.invalid_query = True
            else:
                goods = q_search(query)
                if not goods.exists():
                    self.request.invalid_query = True
                    goods = base_queryset
        else:
            if category_slug == 'all':
                goods = base_queryset
            else:
                goods = base_queryset.filter(category__slug=category_slug)
                if not goods.exists():
                    raise Http404("Товары не найдены в данной категории или по данному запросу.")

        if on_sale: #если передан параметр on_sale, то фильтруем товары по скидке
            goods = goods.filter(discount__gt = 0) #фильтруем товары по скидке, больше 0

        if order_by_prods and order_by_prods != 'default': #если передан параметр order_by, то сортируем товары по цене
            goods = goods.order_by(order_by_prods) #сортируем товары по цене, по возрастанию или убыванию

        return goods


        
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Oak Build - Каталог товаров'
        context['category_slug'] = self.kwargs.get('category_slug') # slug категории, который будет использоваться для фильтрации товаров
        return context
    

class ProductView(DetailView):
    slug_url_kwarg = 'product_slug' # имя параметра в URL  (<slug:product_slug> - после двоиточья) , который будет использоваться для получения slug товара
    template_name = 'goods/product.html'
    context_object_name = 'product'# имя переменной которая будет содержать объект товара в шаблоне

    def get_object(self, queryset = ...):
        product =  Products.objects.get(slug = self.kwargs.get(self.slug_url_kwarg))
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name.capitalize()
        return context




# def catalog(request, category_slug = None):
#     page:str = request.GET.get('page', 1) #получаем номер страницы из запроса, по умолчанию 1
#     on_sale = request.GET.get('on_sale', None) #получаем параметр on_sale из запроса, по умолчанию False
#     order_by_prods = request.GET.get('order_by', None) #получаем параметр order_by из запроса, по умолчанию False
#     query = request.GET.get('q', None) #получаем параметр q из запроса, по умолчанию False

#     if category_slug == 'all':
#         goods = Products.objects.all() #получаем все товары из базы данных
#     elif query: #если передан параметр q, то фильтруем товары по названию
#         goods = q_search(query) #фильтруем товары по названию
#     else:
#         goods = get_list_or_404(Products.objects.filter(category__slug = category_slug)) #получаем товары по slug категории
#         # if not goods.exists(): #если товаров нет, то переадресуем на ютуб или другой сайт, по желанию
#         #    return redirect('https://www.youtube.com/')
    
#     if on_sale: #если передан параметр on_sale, то фильтруем товары по скидке
#         goods = goods.filter(discount__gt = 0) #фильтруем товары по скидке, больше 0

#     if order_by_prods and order_by_prods != 'default': #если передан параметр order_by, то сортируем товары по цене
#         goods = goods.order_by(order_by_prods) #сортируем товары по цене, по возрастанию или убыванию

#     pagin = Paginator(goods, 3)#создание пагинации, по дефолту 3 объекта на странице
    
#     #получаем номер страницы из запроса, если номер страницы больше чем количество страниц, то переходим на последнюю страницу
#     current_page = pagin.page(int(page)) #if int(page)<=pagin.num_pages else pagin.page(pagin.num_pages)

#     context = {
#         'title': 'Oak Build - Каталог товаров',
#         'goods': current_page, #список товаров на текущей странице
#         'category_slug': category_slug, #slug категории
#     }
#     return render(request, 'goods/catalog.html', context=context)



# def product(request, product_slug=False, product_id=False):
#     if product_id: #если передан id товара
#         product = Products.objects.get(id = product_id) #получаем товар по id
#     else:    
#         product = Products.objects.get(slug = product_slug) #получаем товар по slug
#     context = {
#         'product': product,
#     }
#     return render(request, 'goods/product.html', context=context)