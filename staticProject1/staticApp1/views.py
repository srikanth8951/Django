from django.shortcuts import render

# Create your views here.
def view1(request):
    myName = 'Srikanth'
    favPlayer = 'Sachin Tendulkar'
    favAnimal = 'Tiger'
    favSubject = 'Python'
    d = {'name': myName, 'player': favPlayer,'animal': favAnimal,'subject': favSubject}
    return render(request, 'staticApp1/1.html',d)