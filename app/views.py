from django.shortcuts import render

# Create your views here.


def home_view(request):
    data = "home"
    return render(request, 'home.html', {'data': data})


def home_view2(request, year):
    data = str(year)
    return render(request, 'home.html', {'data': data})


def home_view3(request, year, month):
    data = str(year) + ', ' + str(month)
    return render(request, 'home.html', {'data': data})


def home_view4(request, year, month, name):
    data = str(year) + ', ' + str(month) + ', ' + name
    return render(request, 'home.html', {'data': data})


def home_view5(request, page_number):
    data = str(page_number)
    return render(request, 'home.html', {'data': data})


def view_with_default_arg(request, num=1):
    data = str(num)
    return render(request, 'home.html', {'data': data})    
