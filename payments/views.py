from django.http import HttpResponse
from django.shortcuts import render

def payments_view(request):
    return HttpResponse("This is the payments page!")
