from django.http import HttpResponse
from django.shortcuts import render

def users_view(request):
    return HttpResponse("This is the users page!")
