from django.urls import path
from . import views


urlpatterns = [ 
            path('account/', views.show_account, name='account'),
            path('logout/', views.user_logout, name='logout'),
            path('', views.home, name='home'),
            ]