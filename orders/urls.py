from django.urls import path
from . import views


urlpatterns = [ 
            path('cart/', views.show_carts, name='cart'),
            path('add_to_cart/', views.add_to_cart, name='add_to_cart')
               ]