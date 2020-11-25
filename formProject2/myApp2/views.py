from django.shortcuts import render
from myApp2.forms import Feedback
# Create your views here.
def view1(request):
    f = Feedback()
    if request.method=='POST':
        f = Feedback(request.POST)
        if f.is_valid():
            name=f.cleaned_data['name']
            roll=f.cleaned_data['roll']
            email=f.cleaned_data['email']
            comments=f.cleaned_data['comments']
            d={'name1':name,'roll1':roll,'email1':email,'comments1':comments}
            return render(request,'myApp2/output.html',d)
    d={'form':f}
    return render(request,'myApp2/input.html',d)