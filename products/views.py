from django.shortcuts import render

#render html pages

def index(request):
    return render(request, 'index.html')

# return product list
def productList(request):
    return render(request, 'products.html')

# return detailed view of  product
def detailed_product_view(request):
    return render(request, 'product_details.html')