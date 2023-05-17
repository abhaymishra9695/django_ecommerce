"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from store import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('cart/',views.cart,name='cart'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('shop/',views.shop,name='shop'),
    path('contect-us/',views.contectus,name='contectus'),
    path('checkout/',views.checkout,name='checkout'),
    path('singup/',views.singup,name='singup'),
    path('singin/',views.singin,name='singin'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.logout,name='logout'),
    path('seed/',views.seed_data,name='seed'),
    path('product_detail/<slug:slug>',views.product_detail,name='product_detail'),
    path('add_cart_product/<slug:slug>',views.add_cart_product,name='add_cart_product'),
    path('remove_cart_product/<cart_item_id>',views.remove_cart_product,name='remove_cart_product'),
    path('increment_cart/<cart_item_id>',views.increment_cart,name='increment_cart'),
    path('decrement_cart/<cart_item_id>',views.decrement_cart,name='decrement_cart'),
    path('delete_cart',views.delete_cart,name='delete_cart'),
    path('catagory_by_product/<slug:slug>',views.catagory_by_product,name='catagory_by_product'),
    path('search/',views.search,name='search'),
    path('Categories',views.Categories,name='Categories'),
    path('addcategories',views.addcategories,name='addcategories'),
    path('update_category/<slug:slug>',views.update_category,name='update_category'),
    path('delete_category/<slug:slug>',views.delete_category,name='delete_category'),
    path('product',views.product,name='product'),
    path('add_product',views.add_product,name='add_product'),
    path('update_product/<slug:slug>',views.update_product,name='update_product'),
    path('delete_product/<slug:slug>',views.delete_product,name='delete_product'),
    path('slider',views.slider,name='slider'),
    path('add_slider',views.add_slider,name='add_slider'),
    path('edit_slider/<id>',views.edit_slider,name='edit_slider'),
    path('delete_slider/<id>',views.delete_slider,name='delete_slider'),
    path('add-home-page-categories',views.Manage_Home_Categories,name='homepagecategory'),
    path('sale',views.sale,name='sale'),
    path('wishlist/<id>', views.wishlist, name='wishlist'),
    path('deletewishlist/<id>', views.deletewishlist, name='deletewishlist'),
    path('wishlistproduct', views.wishlistproduct, name='wishlistproduct'),
    path('move_to_cart/<slug>', views.move_to_cart, name='move_to_cart'),
    path('coupons',views.coupons,name='coupons'),
    path('add_coupon',views.add_coupon,name='add_coupon'),
    path('edit_coupon/<id>',views.edit_coupon,name='edit_coupon'),
    path('delete_coupon/<id>',views.delete_coupon,name='delete_coupon'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)