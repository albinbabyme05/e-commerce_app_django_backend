from django.shortcuts import render

#render html pages

def index(request):
    return render(request, 'index.html')