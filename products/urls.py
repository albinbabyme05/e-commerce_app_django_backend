from django.urls import path
from . import views


urlpatterns = [ 
               path('', views.index, name='home'),
               path('product_list/', views.productList, name='product_list'),
               path('products_details/', views.detailed_product_view, name='product_details'),
            
            #    path('contact/', views.contact, name='contact'),
            #    path('booking/', views.booking, name='booking'),
               ]