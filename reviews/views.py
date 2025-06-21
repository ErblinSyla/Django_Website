from django.http import HttpResponse
from django.shortcuts import render

def reviews_view(request):
    return HttpResponse("This is the reviews page!")
