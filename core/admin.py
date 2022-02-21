from django.contrib import admin

from .models import Category, Customer, FoodCard, Order
# Register your models here.
admin.site.register(Category)
admin.site.register(FoodCard)
admin.site.register(Order)
admin.site.register(Customer)