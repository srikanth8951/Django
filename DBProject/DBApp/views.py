from django.shortcuts import render
from DBApp.models import Student
# Create your views here.
def view1(request):
    e=Student.objects.all()
    print(type(e))
    d={'emp':e}
    return render(request,'DBApp/1.html',d)