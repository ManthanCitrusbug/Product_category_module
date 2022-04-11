from urllib import request
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views import View
from django.http import JsonResponse
from .models import Category, Product, UserModel, WishList, Cart
from .forms import (SallerRegisterForm, 
                    SallerLoginForm, 
                    CutomerLoginForm, 
                    CustomerRegisterForm, 
                    AddProductForm, 
                    EditProductForm)
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView, DetailView, View
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
        if UserModel.objects.filter(username = user.username, is_seller = True).exists():
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
        new_product.user = self.request.user
        new_product.save()
        return super(AddProductView, self).form_valid(form)


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


class CustomerLoginView(View):
    def post(self,request):
        form = CutomerLoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email,password=password)
        if user is not None: 
            login(request, user)
            return redirect('customer-homepage')
        else:
            return render(request,'customer/customer_login.html',{'form':form}) 

    def get(self,request):
        form = CutomerLoginForm()
        return render(request,'customer/customer_login.html',{'form':form})


class CustomerHomePageView(ListView):
    paginate_by = 5
    model = Product
    context_object_name = 'product_list'
    queryset = Product.objects.all()

    def get_template_names(self):
        return 'customer/cutomer_homepage.html'

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class SearchView(View):
    def get(self, request):
        search = request.GET.get('search')
        qs = Product.objects.filter(product_name__icontains=search)
        data = None
        if len(search)>0 and len(qs)>0:
            data = []
            for p in qs:
                items = {
                    'id':p.id,
                    'name':p.product_name,
                    'discription':p.product_discription,
                    'image':str(p.product_image.url),
                    'price':p.product_price,
                    'category':p.product_category.category_name,
                    'user':p.user.username,
                    'quantity':p.quantity,
                }
                data.append(items)
        else:
            data = 'Nothing Found...'
        return JsonResponse({'data':data})


class WishListView(ListView):
    model = Product
    template_name = 'customer/wish_list.html'
    context_object_name = 'product_list'
    context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['product_list'] = WishList.objects.filter(user=self.request.user)
        return context


class CartView(ListView):
    model = Cart
    template_name = 'customer/add_to_cart.html'
    context_object_name = 'product_list'
    context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['product_list'] = Cart.objects.filter(user=self.request.user)
        price = [p for p in Cart.objects.all() if p.user == self.request.user]
        total = 0
        if price:
            for i in price:
                p = i.products.product_price
                total = total + p
        else:
            pass
        context['total_amount'] = total
        return context


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'customer/details.html'


class AddtoWishListView(View):
    def post(self, request, id):
        product = Product.objects.get(id=id)
        WishList(id=product.id,user=request.user, products=product).save()
        return redirect('wish-list')


class RemovefromWishListView(View):
    def post(self, request, id):
        WishList.objects.get(id=id).delete()
        return redirect('wish-list')


class AddtoCartView(View):
    def post(self, request, id):
        product = Product.objects.get(id=id)
        Cart(id=product.id,user=request.user, products=product).save()
        try:
            WishList.objects.get(id=product.id).delete()
        except:
            return redirect('cart')
        return redirect('wish-list')


class RemovefromCartView(View):
    def post(self, request, id):
        Cart.objects.get(id=id).delete()
        return redirect('cart')

class PlusCartView(View):
    def get(self, request):
        prod_id = request.GET.get('prod_id')
        x = Cart.objects.get(Q(id=prod_id) and Q(user=request.user))
        x.products.quantity+=1
        x.save()
        price = [p for p in Cart.objects.all() if p.user == self.request.user]
        total = 0
        if price:
            for i in price:
                p = i.products.product_price * x.products.quantity
                total = total + p
        else:
            pass
        data = {'quantity':x.products.quantity, 'total':total}
        print(x.products.quantity)
        print(total)
        return JsonResponse({'data':data})

    
class MinusCartView(View):
    def get(self, request):
        prod_id = request.GET.get('prod_id')
        x = Cart.objects.get(Q(id=prod_id) and Q(user=request.user))
        x.products.quantity-=1
        x.save()
        price = [p for p in Cart.objects.all() if p.user == self.request.user]
        total = 0
        if price:
            for i in price:
                p = i.products.product_price * x.products.quantity
                total = total + p
        else:
            pass
        data = {'quantity':x.products.quantity, 'total':total}
        print(x.products.quantity)
        print(total)
        return JsonResponse({'data':data})