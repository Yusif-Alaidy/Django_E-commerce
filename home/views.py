from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .models          import *
from .forms           import *

def home(request):

    categories      = category.objects.all()
    products        = product.objects.all()
    active_category = request.GET.get('category', '')
    
    if active_category:
        products = products.filter(category__catslug=active_category)
    context = {
        'product'         : products,
        'categories'      : categories,
        'active_category' : active_category
    }
    return render(request, 'index.html', context)

def blog_details(request):    
    categories      = category.objects.all()
    products        = product.objects.all()
    active_category = request.GET.get('category', '')
    
    if active_category:
        products = products.filter(category__catslug=active_category)
    context = {
        'product'         : products,
        'categories'      : categories,
        'active_category' : active_category
    }
    return render(request, 'blog-details.html', context)

def blog(request):
    categories      = category.objects.all()
    products        = product.objects.all()
    active_category = request.GET.get('category', '')
    
    if active_category:
        products = products.filter(category__catslug=active_category)
    context = {
        'product'         : products,
        'categories'      : categories,
        'active_category' : active_category
    }
    return render(request, 'blog.html', context)

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')


def shop_grid(request):
    return render(request, 'shop-grid.html')

def shoping_cart(request):
    return render(request, 'shoping-cart.html')

def search_product(request):
    if request.method == 'POST':
        search = request.POST['search']
        ps = product.objects.filter(title__contains=search)
        context={
        'ps':ps,
        'category':category
    }
        return render(request, 'search_product.html', context)
    else:
        return render(request, 'search_product.html')

def shop_details(request,slug):
    prod = get_object_or_404(product, slug=slug)
    
    # getting all review
    reviews = Review.objects.filter(Product=prod)
    
    # getting average review
    average_rating = Review.objects.filter(Product=prod).aggregate(rating=Avg('rate'))
    average_rating = int(average_rating['rating'])
    context = {
        'product'  : prod,
        'reviews'  : reviews,
        'category' : category,
        'average_rating'  : average_rating,              
        }
    return render(request, 'shop-details.html', context)


