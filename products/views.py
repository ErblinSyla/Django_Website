from django.http import HttpResponse
from django.shortcuts import render

def products_view(request):
    return HttpResponse("This is the products page!")
