"""django_urls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path, register_converter
from app import views
from app.utils import FourDigitYearConverter

register_converter(FourDigitYearConverter, "yyyy")

urlpatterns = [
    # path('admin/', admin.site.urls),

    # Home page: only slash
    path('', views.home_view1),

    # Static urls: 2003
    path('articles/2023/', views.home_view2),

    # Dinamic urls: accept int 
    path('articles/<int:year>/', views.home_view2),

    # Dinamic urls accept year/month
    path('articles/<int:year>/<int:month>/', views.home_view3),

    # Dinamic urls accept year/month/slug
    path('articles/<int:year>/<int:month>/<str:name>/', views.home_view4),

    # Dinamic urls that start with articles and with optional int value at the end
    re_path(r"^books/(?:page-(?P<page_number>[0-9]+)/)?$", views.home_view),  
    re_path(r"^books/(?P<year>[0-9]{4})/$", views.home_view),
    re_path(r"^books/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$", views.home_view),

    # Dinamic Customized parameter 
    path("articles/<yyyy:year>/", views.home_view2),

    # Dinamic url that only change number of last part
    path("blog/page<int:num>/", views.view_with_default_arg), # With default argument in View

    # Including urls from other app
    path("app/", include("app.urls")),
]
