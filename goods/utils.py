from django.db.models import Q

from goods.models import Products

def q_search(query):
    if query.isdigit() and len(query) <=5:  # если поиск осуществляется по id товара
        return Products.objects.filter(id = int(query))
    
    key_words = [word for word in query.split() if len(word) >2]  # убираем слова меньше 3 символов

    q_filters = Q()

    for word in key_words:
        q_filters |= Q(description__icontains = word)
        q_filters |= Q(name__icontains = word)

    return Products.objects.filter(q_filters)

