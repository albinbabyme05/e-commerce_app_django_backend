from django.shortcuts import render

# custmorer

def show_account(request):
    return render(request, 'account.html')
