from django.shortcuts import render

# Create your views here.


def home_view1(request):
    data = {}
    return render(request, 'home.html', {'data': data})


def home_view2(request, year):
    data = {}
    return render(request, 'home.html', {'data': data})


def home_view3(request, year, month):
    data = {}
    return render(request, 'home.html', {'data': data})


def home_view4(request, year, month, name):
    data = {}
    return render(request, 'home.html', {'data': data})


def view_with_default_arg(request, num=1):
    data = {}
    return render(request, 'home.html', {'data': data})    
