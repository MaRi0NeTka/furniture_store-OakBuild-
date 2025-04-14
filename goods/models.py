from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True,null=True, blank=True, verbose_name='URL')
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию' #имя которое отображается в таблице в админке
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True,null=True, blank=True, verbose_name='URL')
    description = models.TextField(verbose_name='Описание',blank=True, null=True, default='Здесь может быть ваша реклама',)
    image = models.ImageField(upload_to='goods_media', verbose_name='Изображение', blank=True, null=True)
    price = models.DecimalField(default = 0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default= 0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    quatity= models.PositiveIntegerField(default= 0, verbose_name='Количество')
    category = models.ForeignKey(Categories, on_delete= models.CASCADE, verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')


    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт' #имя которое отображается в таблице в админке
        verbose_name_plural = 'Продукты'

    def __str__(self): #переопределяем метод __str__ чтобы в админке отображалось имя товара
        return f'{self.name} Количество - {self.quatity}'
    
    def display_id (self):
        # метод для отображения id товара
        return f'{self.id:05}'
    
    
    def get_sell_price(self):
        new_price = self.price - (self.price * self.discount )
        self.discount = self.discount * 100 #приводим к процентам (старое отображение 0.2, новое 20%)
        return round(new_price, 2) #округляем до 2 знаков после запятой