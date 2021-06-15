from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse("Home page of app_2")

def product(request):
    return HttpResponse("Product page of app_2")

def customer(request):
    return HttpResponse("Customer page of app_2")
