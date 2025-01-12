from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as auth_logout
from .models import Customer

def show_account(request):
    # Handle Registration
    if request.POST and 'register' in request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose a different username.")
            return render(request, 'account.html')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return render(request, 'account.html')

        # Create the User
        user_reg = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        
        # Create Customer record
        Customer.objects.create(
            user=user_reg,
            phone=phone
        )
        messages.success(request, "Registration successful! You can now log in.")
        return redirect('account')  # Redirect back to the account page for login

    # Handle Login
    elif request.POST and 'login' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the homepage or dashboard
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'account.html') 

    # Render the account page for GET requests
    return render(request, 'account.html')


def user_logout(request):
    auth_logout(request)
    return redirect('home')
  
  
def home(request):
    return render(request, 'index.html')
