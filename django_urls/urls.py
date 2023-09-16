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
    path('', views.home_view),
    path('articles/2003/', views.home_view),
    path('articles/<int:year>/', views.home_view),
    path('articles/<int:year>/<int:month>/', views.home_view),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.home_view),
    re_path(r"^articles/(?:page-(?P<page_number>[0-9]+)/)?$", views.home_view),
    re_path(r"^articles/(?P<year>[0-9]{4})/$", views.home_view),
    re_path(r"^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$", views.home_view),
    path("articles/<yyyy:year>/", views.home_view),
    path("blog/page<int:num>/", views.view_with_default_arg), # With default argument in View
    path("app/", include("app.urls")),
]
