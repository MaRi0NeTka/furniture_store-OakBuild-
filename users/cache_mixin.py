from django.core.cache import cache


class CacheMixin:
    def get_set_cache(self, query, cache_name, time=60):
        """
        Получает данные из кэша или из базы данных, если кэш пуст.
        :param query: Запрос к базе данных.
        :param cache_name: Имя кэша.
        :param time: Время жизни кэша в секундах.
        :return: Данные из кэша или из базы данных.
        """
        data = cache.get(cache_name)
        if not data:
            data = query
            cache.set(cache_name, data, time)
        return data
