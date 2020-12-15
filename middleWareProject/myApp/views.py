from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
    print('Inside View Function')
    return HttpResponse('<h1>output on browser</h1>')
