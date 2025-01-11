from django.urls import path
from . import views


urlpatterns = [ 
               path('', views.index, name='home'),
               path('product_list/', views.productList, name='product_list'),
               path('products_details/<pk>', views.detailed_product_view, name='product_details'),
               ]