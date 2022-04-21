from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from .models import Product, WishList

@receiver(user_logged_in, sender=UserModel)
def user_login(sender, request, user, **kwargs):
    print(user,"login...")
    print(request)

@receiver(user_logged_out, sender=UserModel)
def user_login(sender, request, user, **kwargs):
    print(user,"logout...")
    print(request)

@receiver(user_login_failed)
def user_login(sender, credentials ,request, **kwargs):
    print(credentials,"login failed...")
    print(request)

@receiver(post_save, sender=Product)
def product_qun(sender, instance, **kwargs):
    # wish = WishList.objects.filter(user=request.user)
    # print(wish)
    instance.save()
    print("Quantity updated...")
