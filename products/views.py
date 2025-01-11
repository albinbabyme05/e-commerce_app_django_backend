from django.shortcuts import render, redirect
from . models import Product

# implimetting pagiator
from django.core.paginator import Paginator

#render html pages

def index(request):
    featured_products = Product.objects.order_by('priority')[:4] 
    latest_products = Product.objects.order_by('-id')[:4] 
    context = {
        'featured_products' : featured_products,
        'latest_products' :    latest_products
            }
    return render(request, 'index.html', context)

# return product list
def productList(request):
    #base on the user request fetching the page
    page = 1
    
    if request.GET:
        page = request.GET.get('page', 1)
    
    product_list  = Product.objects.order_by('priority') 
    
    product_paginator  =  Paginator(product_list, 3)
    product_list = product_paginator.get_page(page)
    
    product_dict = {'products' : product_list}
    return render(request, 'products.html', product_dict)

# return detailed view of  product
def detailed_product_view(request, pk):
    #fetch the product
    product = Product.objects.get(pk=pk)
    context = {'product' : product}
    return render(request, 'product_details.html', context)