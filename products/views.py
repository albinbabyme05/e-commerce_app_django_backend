from django.shortcuts import render, redirect
from . models import Product

# implimetting pagiator
from django.core.paginator import Paginator

#render html pages

def index(request):
    return render(request, 'index.html')

# return product list
def productList(request):
    #base on the user request fetching the page
    page = 1
    
    if request.GET:
        page = request.GET.get('page', 1)
    
    product_list  = Product.objects.all() 
    
    product_paginator  =  Paginator(product_list, 1)
    product_list = product_paginator.get_page(page)
    
    product_dict = {'products' : product_list}
    return render(request, 'products.html', product_dict)

# return detailed view of  product
def detailed_product_view(request):
    return render(request, 'product_details.html')