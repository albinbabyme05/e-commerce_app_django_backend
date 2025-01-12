from django.shortcuts import render, redirect
from . models import Orders, OrderItems, Product

# Create your views here.
def show_carts(request):
    return render(request, 'cart.html')

def add_to_cart(request):
    if request.POST:
        user=request.user
        customer = user.customer_profile
        quantity = int(request.POST.get('quanitiy'))
        size = str(request.POST.get('size'))
        product_id = request.POST.get('product_id')
        cart_obj, created =  Orders.objects.get_or_create(
            owner = customer,
            orderStatus = Orders.CART_STAGE
        )
        product_obj = Product.objects.get(pk=product_id)
        ordered_items = OrderItems.objects.create(
            product = product_obj,
            owner=cart_obj,
            quantity = quantity,
            size = size
        )
        return redirect('cart')