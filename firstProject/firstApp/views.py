from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def my_display(request):
     s = 'Hello World'
     return HttpResponse(s)
