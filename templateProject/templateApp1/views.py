from django.shortcuts import render

# Create your views here.
def my_views(request):
    return render(request, 'templatesApp1/1.html')