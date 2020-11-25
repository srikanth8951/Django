from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
    s = '<h1>'+'Welcome to the world of python Web Development'+'</h1>'
    return HttpResponse(s)
