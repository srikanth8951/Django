from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
    s = '<h1>'+'This is 1st response'+'</h1>'
    return HttpResponse(s)
def view2(request):
    s = '<h1>'+'This is 2nd response'+'</h1>'
    return HttpResponse(s)
def view3(request):
    s = '<h1>'+'This is 3rd response'+'</h1>'
    return HttpResponse(s)
