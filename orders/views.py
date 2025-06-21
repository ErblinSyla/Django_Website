from django.http import HttpResponse
from django.shortcuts import render

def orders_view(request):
    return HttpResponse("This is the orders page!")
