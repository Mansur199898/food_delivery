from itertools import product
from sre_constants import MAX_UNTIL
from termios import TAB3
from django.db import models
from django.forms import CharField


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Категория')
    def __str__(self):
        return self.title
# Create your models here.
class  FoodCard(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название еды')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='core', verbose_name='Изобраажение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    message = models.TextField()

class Order(models.Model):
    product = models.ForeignKey(FoodCard, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
