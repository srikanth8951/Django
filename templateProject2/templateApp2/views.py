from django.shortcuts import render

# Create your views here.
def employeeView(request):
    Ename = input('Enter the name')
    Edesignation = input('Enter the designation')
    Eexp = float(input('Enter the Exeperience'))
    Esalary = int(input('Enter the Salary'))
    d = {'name':Ename, 'desig':Edesignation,'exp':Eexp,'sal':Esalary}
    return render(request, 'templatesApp2/1.html',d)