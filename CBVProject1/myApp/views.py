from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from myApp.models import Student
from django.urls import reverse_lazy

# Create your views here.
class StudentListView(ListView):
    model=Student
    #default template=student_list.html
    #default context=student_list 
    #context=dict

class StudentDetailView(DetailView):
    model=Student
    #default template=student_detail.html
    #default context=student

class StudentCreateView(CreateView):
    #default template=student_form.html
    model=Student
    fields=('name','number','marks','place')

class StudentUpdateView(UpdateView):
    #default template=student_form.html
    model=Student
    fields=('name','marks','place')

class StudentDeleteView(DeleteView):
    #default template=student_confirm_delete.html
    model=Student
    success_url=reverse_lazy('students')