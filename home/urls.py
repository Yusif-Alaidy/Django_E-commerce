from django.urls import path 
from . import views

app_name='home'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path('blog', views.blog, name='blog'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('shop_details/<slug:slug>', views.shop_details, name='shop_details'),
    path('shop_grid', views.shop_grid, name='shop_grid'),
    path('shoping_cart', views.shoping_cart, name='shoping_cart'),
    path('search_product', views.search_product, name='search_product'),

    # add review
    path('ajax-add-review/<slug:slug>/', views.ajax_add_review, name="ajax-add-review")
    
]
