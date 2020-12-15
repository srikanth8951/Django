from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'myApp/home.html')

def java_view(request):
    return render(request,'myApp/javaexams.html')