from django.shortcuts import render

# Create your views here.


def home_view(request):
    data = {}
    return render(request, 'home.html', {'data': data}) 
