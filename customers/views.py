from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from . models import Customer

# custmorer

def show_account(request):
    if request.POST and 'register' in request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        address = request.POST.get('address')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose a different username.")
            return render(request, 'account.html')

        # Check if email already exists (optional)
        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return render(request, 'account.html')
        
        user_reg = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        print(user_reg)
        #create customer and model
        customer=Customer.objects.create(
            user=user_reg,
            phone=phone,
            address=address
        )
        return redirect('home')
        
        
    return render(request, 'account.html')
