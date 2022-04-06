from dataclasses import field
from pyexpat import model
from django.contrib import admin
from .models import UserModel, Product, Category
# Register your models here.

class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'email', 'be_a_customer']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'product_discription', 'product_price', 'user']

admin.site.register(UserModel,UserModelAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)