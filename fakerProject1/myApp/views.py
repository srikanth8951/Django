from django.shortcuts import render
from myApp.models import Student
# Create your views here.
def view1(request):
    #s=Student.objects.filter(marks__gt=40) greater than #QuerrySet
    #s=Student.objects.filter(marks__lt=40) less than
    #s=Student.objects.filter(marks__lte=18) less than or equal
    #s=Student.objects.filter(marks__gte=20) greater than or equal
    #s=Student.objects.filter(marks__exact=20)
    #s=Student.objects.filter(name__exact="Logan Miller")
    #s=Student.objects.filter(name__iexact="logan Miller")
    #s=Student.objects.filter(name__exact="Logan Miller")
    #s=Student..objects.exclude(marks_range=(40,50))
    s=Student.objects.all()
    d={'stud':s}
    return render(request,'myApp/1.html',d)
