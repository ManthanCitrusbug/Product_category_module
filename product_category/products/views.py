from pyexpat import model
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View

import products
from .models import Category, Product, UserModel, WishList
from .forms import (SallerRegisterForm, 
                    SallerLoginForm, 
                    CutomerLoginForm, 
                    CustomerRegisterForm, 
                    AddProductForm, 
                    EditProductForm)
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView


#-----------------------------------------------------------------------------------------------------------------------------
# INDEX VIEW    
#-----------------------------------------------------------------------------------------------------------------------------

class IndexView(TemplateView):
    template_name = 'index.html'

#-----------------------------------------------------------------------------------------------------------------------------
# Saller VIEW    
#-----------------------------------------------------------------------------------------------------------------------------

class SallerRegisterView(CreateView):
    model = UserModel
    form_class = SallerRegisterForm
    template_name = 'saller/saller_register.html'
    success_url = 'saller-login'


class SallerLoginView(View):
    def post(self,request):
        form = SallerLoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email,password=password)
        if user is not None:
            login(request, user)
            return redirect('saller-dashboard')
        else:
            return render(request,'saller/saller_login.html',{'form':form})
    def get(self,request):
        form = SallerLoginForm()
        return render(request,'saller/saller_login.html',{'form':form})


class SallerLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('/')


class SallerDashboardView(ListView):
    model = Product
    template_name = 'saller/saller_dashboard.html'
    context_object_name = 'product_list'
    context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['product_list'] = Product.objects.filter(user = self.request.user)
        return context


class AddProductView(CreateView):
    model = Product
    form_class = AddProductForm
    template_name = 'saller/add_product.html'
    success_url = 'saller-dashboard'

    def form_valid(self, form):
        new_product = form.save(commit=False)
        prod = UserModel.objects.get(username = self.request.user)
        new_product.user = prod
        new_product.save()
        return super (AddProductView, self).form_valid(form)


class EditProductView(UpdateView):
    model = Product
    form_class = EditProductForm
    template_name = 'saller/edit_product.html'
    success_url = reverse_lazy('saller-dashboard')


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'saller/delete_product.html'
    success_url = reverse_lazy('saller-dashboard')

#-----------------------------------------------------------------------------------------------------------------------------
# Customer VIEW    
#-----------------------------------------------------------------------------------------------------------------------------

class CustomerRegisterView(CreateView):
    model = UserModel
    form_class = CustomerRegisterForm
    template_name = 'customer/customer_register.html'
    success_url = 'customer-login'

    def form_valid(self, form):
        new_product = form.save(commit=False)
        new_product.be_a_customer = True
        new_product.save()
        return super (CustomerRegisterView, self).form_valid(form)


class CustomerLoginView(View):
    def post(self,request):
        form = CutomerLoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email,password=password)
        if user is not None and UserModel.objects.get(username=user, be_a_customer=True):
            login(request, user)
            # return render(request,'customer/customer_homepage.html')
            return redirect('customer-homepage')
        else:
            return render(request,'customer/customer_login.html',{'form':form}) 

    def get(self,request):
        form = CutomerLoginForm()
        return render(request,'customer/customer_login.html',{'form':form})


# class CustomerHomepageView(ListView):
#     model = Product
#     template_name = 'customer/customer_homepage.html'
#     context_object_name = 'product_list'
#     context = {}

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category'] = Category.objects.all()
#         context['product_list'] = Product.objects.all()
#         return context

class CustomerHomePageView(ListView):
    model = Product
    context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['product_list'] = Product.objects.all()
        return context

    def get_template_names(self):
        return 'customer/cutomer_homepage.html'


class AddtoWishListView(ListView):
    model = WishList
    template_name = 'customer/wish_list.html'
    # context = {}
    success_url = 'customer-homepage'

    # def get(self, request, id):
    #     product = Product.objects.get(id=id)
    #     product.wish_list = True
    #     return product
        
