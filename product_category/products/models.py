from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, username, password = None):
        if not email:
            raise ValueError("Enter your email.")
        if not username:
            raise ValueError("Enter your username.")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_superuser(self, email, username, password = None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )

        user.is_active = True
        user.is_admin  = True
        user.is_staff  = True
        user.is_superuser = True

        user.save(using = self.db)
        return user


class UserModel(AbstractBaseUser,PermissionsMixin):
    username                = models.CharField(max_length=70, unique=True)
    first_name              = models.CharField(max_length=70)
    last_name               = models.CharField(max_length=70)
    email                   = models.EmailField(max_length=70, unique=True)
    profile_image           = models.ImageField(upload_to = 'image/', default = 'media/image/defualt_img.jpeg')
    be_a_customer           = models.BooleanField(default=False)

    is_active               = models.BooleanField(default=True)
    is_admin                = models.BooleanField(default=False)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username


class Category(models.Model):
    category_name                  = models.CharField(max_length=70)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name                   = models.CharField(max_length=100)
    product_discription            = models.TextField()
    product_image                  = models.ImageField(upload_to = 'image/', default = 'media/image/defualt_img.jpg')
    product_price                  = models.PositiveIntegerField()
    # product_quantity               = models.IntegerField(default=1)
    product_category               = models.ForeignKey(Category, on_delete=models.CASCADE)
    user                           = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    wish_list                      = models.BooleanField(default=False)
    # product_name                   = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name


class WishList(models.Model):
    products                        = models.ForeignKey(Product, on_delete=models.CASCADE)
    user                            = models.ForeignKey(UserModel, on_delete=models.CASCADE)

