from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def home_view(request):
    return render(request,'myApp/home.html')
@login_required
def java_view(request):
    return render(request,'myApp/javaexams.html')
@login_required
def python_view(request):
    return render(request,'myApp/pythonexams.html')
@login_required
def aptitude_view(request):
    return render(request,'myApp/aptitudeexams.html')

def logout_view(request):
    return render(request,'myApp/logout.html')