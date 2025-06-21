from django.http import HttpResponse
from django.shortcuts import render

def cart_view(request):
    return HttpResponse("This is the cart page!")
