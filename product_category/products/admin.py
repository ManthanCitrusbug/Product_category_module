from dataclasses import field
from pyexpat import model
from django.contrib import admin
from .models import UserModel, Product, Category, WishList, Cart, OrderedProducts, Comments
# Register your models here.

class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'email']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'product_discription', 'product_price', 'quantity', 'user']

class WishListAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'products', 'quantity']

class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'products', 'quantity']

class OrderedProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'products', 'quantity']

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['rate', 'comments', 'user', 'products']


admin.site.register(UserModel,UserModelAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(WishList,WishListAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(OrderedProducts,OrderedProductsAdmin)
admin.site.register(Comments,CommentsAdmin)

