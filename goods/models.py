from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name = 'Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null = True, verbose_name = 'URL')
    # max_length=150 длинна. unique=True уникальность. blank=True поле может быть пустым. null = True  
    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
    
    def __str__(self): # для того чтобы в админ панели новые категории назывались по названию
        return self.name
    

class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name = 'Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null = True, verbose_name = 'URL')
    description = models.TextField(blank=True, null=True,verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name = 'Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name = 'Цена')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name = 'Скидка в процентах')
    quantity = models.PositiveIntegerField(default=0, verbose_name = 'Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name = 'Категория') # Связь с картами, при удалении карты удалятся и эти данные 

    # IntegerField - любое число. PositiveIntegerField - положительное число
    # max_digits сколько знаков до запятой
    # decimal_places сколько знаков после запятой
    # DecimalField для цифр с плавающей точкой  
    # CharField для коротких текстов, 
    # TextField для длинных

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ("id",)

    def __str__(self): # для того чтобы в админ панели новые продукты назывались по названию, и указывалось их количество
        return f'{self.name} Количество - {self.quantity}' 
        
    def display_id(self):  # для того чтобы id имели больше нулей 00004
        return f"{self.id:05}"
    
    def total_price(self): # расчет цены с учетом скидки
        if self.discount:
            return round(self.price - self.price * self.discount/100, 2)
        return self.price
     