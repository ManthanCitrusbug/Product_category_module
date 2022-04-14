from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views import View
from django.http import JsonResponse, HttpResponse

from .models import Category, Product, UserModel, WishList, Cart
from .forms import (SallerRegisterForm, 
                    SallerLoginForm, 
                    CutomerLoginForm, 
                    CustomerRegisterForm, 
                    AddProductForm, 
                    EditProductForm)
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DetailView, View
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
            msg = "Invalid details"
            return render(request,'saller/saller_login.html',{'form':form, 'msg':msg})

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
    context_object_name = 'seller_list'
    context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['seller_list'] = Product.objects.filter(user = self.request.user)
        return context


class AddProductView(CreateView):
    model = Product
    form_class = AddProductForm
    template_name = 'saller/add_product.html'
    success_url = 'saller-dashboard'

    def form_valid(self, form):
        image = form.cleaned_data.get('product_image')
        new_product = form.save(commit=False)
        new_product.user = self.request.user
        new_product.product_image = image
        new_product.save()
        return super(AddProductView, self).form_valid(form)


class SellerCategoryView(View):
    def get(self, request):
        id = request.GET.get('id')
        cat_filter = Category.objects.get(id=id)
        qs = Product.objects.filter(product_category=cat_filter, user=request.user)
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
        print(data)
        return JsonResponse({'data':data})

    
class SellerSearchView(View):
    def get(self, request):
        search = request.GET.get('search')
        print(search)
        qs = Product.objects.filter(product_name__icontains=search, user=request.user)
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


class EditProductView(UpdateView):
    model = Product
    form_class = EditProductForm
    template_name = 'saller/edit_product.html'
    success_url = reverse_lazy('saller-dashboard')


class SellerProductDetailsView(DetailView):
    model = Product
    template_name = 'saller/seller_product_detail.html'


class DeleteProductView(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        product.is_deleted = True
        product.save()
        return render(request,'saller/saller_dashboard.html')


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
            msg = "Invalid details"
            return render(request,'customer/customer_login.html',{'form':form, 'msg':msg}) 

    def get(self,request):
        form = CutomerLoginForm()
        return render(request,'customer/customer_login.html',{'form':form})


class CustomerHomePageView(ListView):
    paginate_by = 5
    model = Product
    context_object_name = 'product_list'
    ordering = ['id']
    queryset = Product.objects.filter(is_deleted = False)

    def get_template_names(self):
        return 'customer/cutomer_homepage.html'

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_products'] = Product.objects.all().count
        context['category'] = Category.objects.all()
        context['cart'] = Cart.objects.filter(user=self.request.user).values_list("products__id", flat=True)
        context['wishlist'] = WishList.objects.filter(user=self.request.user).values_list("products__id", flat=True)
        return context


class SearchView(View):
    def get(self, request):
        search = request.GET.get('search')
        print(search)
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
    context_object_name = 'wish_list'
    ordering = ['id']
    context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['wish_list'] = WishList.objects.filter(user=self.request.user)
        return context


class CartView(ListView):
    model = Cart
    template_name = 'customer/add_to_cart.html'
    context_object_name = 'cart_list'
    ordering = ['id']
    context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['cart_list'] = Cart.objects.filter(user=self.request.user)
        return context


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'customer/details.html'


class AddtoWishListView(View):
    def post(self, request, id):
        product = Product.objects.get(id=id)
        WishList(user=request.user,products=product).save()
        return redirect('wish-list')


class RemovefromWishListView(View):
    def post(self, request, id):
        WishList.objects.get(id=id).delete()
        return redirect('wish-list')


class AddtoCartView(View):
    def post(self, request, id):
        product = Product.objects.get(id=id)
        Cart(user=request.user, products=product).save()
        WishList.objects.filter(products__id=id, user=request.user).delete()
        return redirect('cart')


class RemovefromCartView(View):
    def post(self, request, id):
        Cart.objects.get(id=id).delete()
        return redirect('cart')


class CategoryView(View):
    def get(self, request):
        id = request.GET.get('id')
        cat_filter = Category.objects.get(id=id)
        qs = Product.objects.filter(product_category=cat_filter)
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
        print(data)
        return JsonResponse({'data':data})


class PlusCartView(View):
    def get(self, request):
        prod_id = request.GET.get('id')
        prod_qun = request.GET.get('quantity')
        print(int(prod_qun))
        prod_cat = Cart.objects.filter(id=prod_id)
        print(prod_cat)
        return JsonResponse({'data':"done..."})