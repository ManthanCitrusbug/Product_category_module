"""product_category URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.IndexView.as_view(),name='index'),
#---------------------------------------------------------------------------------------------------------------------------
    path('saller-register',views.SallerRegisterView.as_view(), name='saller-register'),
    path('saller-login', views.SallerLoginView.as_view(), name='saller-login'),
    path('saller-logout', views.SallerLogoutView.as_view(), name='saller-logout'),
    path('saller-dashboard', views.SallerDashboardView.as_view(), name='saller-dashboard'),
    path('add-product', views.AddProductView.as_view(), name='add-product'),
    path('edit-product/<int:pk>', views.EditProductView.as_view(), name = 'edit-product'),
    path('delete-product/<int:pk>', views.DeleteProductView.as_view(), name = 'delete-product'),
#----------------------------------------------------------------------------------------------------------------------------
    path('customer-register',views.CustomerRegisterView.as_view(), name='customer-register'),
    path('customer-login', views.CustomerLoginView.as_view(), name='customer-login'),
    path('customer-homepage', views.CustomerHomePageView.as_view(), name='customer-homepage'),
    path('wish-list', views.WishListView.as_view(), name='wish-list'),
    path('cart', views.CartView.as_view(), name='cart'),
    path('add-to-wish-list/<int:id>',views.AddtoWishListView.as_view(), name='add-to-wish-list'),
    path('add-to-cart/<int:id>',views.AddtoCartView.as_view(), name='add-to-cart'),
    path('remove-from-wish-list/<int:id>',views.RemovefromWishListView.as_view(), name='remove-from-wish-list'),
    path('remove-from-cart/<int:id>',views.RemovefromCartView.as_view(), name='remove-from-cart'),
    path('details/<int:pk>',views.ProductDetailsView.as_view(),name='details'),
    path('search', views.SearchView.as_view(), name='search'),
    path('plus-cart', views.PlusCartView.as_view(), name='plus-cart'),
    path('minus-cart', views.MinusCartView.as_view(), name='minus-cart'),


] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
