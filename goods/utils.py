from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from rapidfuzz import fuzz


from goods.models import Products

"""Принцип поиска заключается в Fuzzy Wuzzer, который позволяет находить слова, которые похожи на искомое слово."""


def q_search(query):
    if query.isdigit() and len(query) <=5:  # если поиск осуществляется по id товара
        return Products.objects.filter(id = int(query))
    
    goods = Products.objects.all()
    results = []

    for product in goods:
        ratio = fuzz.partial_ratio(query.lower(), product.name.lower())
        ratio2 = fuzz.partial_ratio(query.lower(), product.description.lower())
        if ratio > 90:  # допустим, 70% совпадения
            results.append((ratio, product))
        elif ratio2 > 80:
            results.append((ratio2, product))

    # Сортируем по степени совпадения
    results.sort(key=lambda x: x[0], reverse=True)
    
    return [product for ratio, product in results]


"""Тоже самое, только с использованием Postgres."""

    # vector = SearchVector('name', 'description')  # создаем вектор поиска по полям name и description
    # query = SearchQuery(query)  # создаем запрос поиска

    # return Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt = 0).order_by('-rank')  # поиск по вектору
    
    # key_words = [word for word in query.split() if len(word) >2]  # убираем слова меньше 3 символов

"""Равноценный поиск по всем полям."""
    # q_filters = Q()

    # for word in key_words:
    #     q_filters |= Q(description__icontains = word)
    #     q_filters |= Q(name__icontains = word)

    # return Products.objects.filter(q_filters)

