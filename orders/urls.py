from django.urls import path
from . import views


urlpatterns = [ 
            path('cart/', views.show_carts, name='cart'),
               ]