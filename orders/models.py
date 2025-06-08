from django.db import models

from goods.models import Products
from users.models import User

class OrderItemQuerySet(models.QuerySet): #расширяем стандартный QuerySet и добавляем методы

    def get_total_price(self):
        return sum(item.products_price() for item in self)
    
    def get_quantity(self):
        if self:
            return sum(item.quantity for item in self)
        return 0
    
class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, default=None, verbose_name='Пользователь')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    requires_delivery = models.BooleanField(default=False, verbose_name='Требуется доставка')
    delivery_adress = models.TextField(blank=True, null=True, verbose_name='Адрес доставки')    
    payment_on_get =models.BooleanField(default=False, verbose_name='Оплата при получении')
    is_paid = models.BooleanField(default=False, verbose_name='Оплачено')
    status = models.CharField(max_length=50, default='В обработке', verbose_name='Статус заказа')

    class Meta:
        db_table = 'orders'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    objects = OrderItemQuerySet.as_manager() #расширяем стандартный менеджер модели
    def __str__(self):
        return f'Заказ №{self.pk} | Пользователь: {self.user.username} | Статус: {self.status}'
    

class OrderItem(models.Model):
    # related_name отвечает за обратную связь, чтобы можно было получить все элементы заказа через Order
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name='items', verbose_name='Заказ')
    product = models.ForeignKey(to=Products, on_delete=models.SET_DEFAULT, null=True, default=None, verbose_name='Товар')
    name = models.CharField(max_length=150, verbose_name='Название товара')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена товара')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        db_table = 'order_items'
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'

    objects = OrderItemQuerySet.as_manager()  # расширяем стандартный менеджер модели
    def __str__(self):
        return f'Заказ №{self.order.pk} | Товар: {self.name} | Количество: {self.quantity}'
    
    def products_price(self):
        return round(self.price * self.quantity, 2)