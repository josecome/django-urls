from django.urls import path
from . import views

urlpatterns = [
    path('test', views.home_view),
]