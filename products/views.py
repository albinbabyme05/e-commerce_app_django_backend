from django.shortcuts import render
from . models import Product

#render html pages

def index(request):
    return render(request, 'index.html')

# return product list
def productList(request):
    product_dict = {
        'products' : Product.objects.all()
    }
    return render(request, 'products.html', product_dict)

# return detailed view of  product
def detailed_product_view(request):
    return render(request, 'product_details.html')