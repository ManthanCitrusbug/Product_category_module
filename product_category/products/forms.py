from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Category, Product, UserModel

#-----------------------------------------------------------------------------------------------------------------------------
# Saller Form   
#-----------------------------------------------------------------------------------------------------------------------------

class SallerRegisterForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_image', 'password']
        widgets = {
            'username' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'first_name' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'last_name' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'email' : forms.EmailInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'profile_image' : forms.FileInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'password' : forms.PasswordInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            )
        }
        

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_seller = True
        if commit:
            user.save()
        return user
        


class SallerLoginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['email', 'password']
        widgets = {
            'email' : forms.EmailInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'password' : forms.PasswordInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            )
        }

#-----------------------------------------------------------------------------------------------------------------------------
#   
#-----------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------
# Customer Form    
#-----------------------------------------------------------------------------------------------------------------------------

class CustomerRegisterForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_image', 'password']
        widgets = {
            'username' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'first_name' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'last_name' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'email' : forms.EmailInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'profile_image' : forms.FileInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'password' : forms.PasswordInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            )
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class CutomerLoginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['email', 'password']
        widgets = {
            'email' : forms.EmailInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'password' : forms.PasswordInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            )
        }

#-----------------------------------------------------------------------------------------------------------------------------
# 
#-----------------------------------------------------------------------------------------------------------------------------

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_discription', 'product_image', 'product_category', 'product_price', 'quantity']
        widgets = {
            'product_name' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'product_discription' : forms.Textarea(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'product_image' : forms.FileInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'product_category' : forms.Select(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'product_price' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'quantity' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
 
        }


class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_discription', 'product_image', 'product_price', 'product_category']
        widgets = {
            'product_name' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'product_discription' : forms.Textarea(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'product_image' : forms.FileInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'product_category' : forms.Select(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'product_price' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
        }
