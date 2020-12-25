from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from myApp.forms import EmailSendForm
from django.core.mail import send_mail
from myApp.models import Post
def post_list_view(request):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,2) #step1
    page_number=request.GET.get('page') #step2
    try:
       post_list=paginator.page(page_number) #step2
    except PageNotAnInteger:
       post_list=paginator.page(1) #step 3
    except EmptyPage:
      post_list=paginator.page(paginator.num_pages) #step 4
    d={'post_list':post_list}
    return render(request,'myApp/post_list.html',d)
def post_detail_view(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,publish__year=year,publish__month=month,publish__day=day)
    d={'post':post}
    return render(request,'myApp/post_detail.html',d)
def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    form=EmailSendForm()
    if request.method=='POST':
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            #READ THE DATA SEND MAIL
    d={'post':post,'form':form}
    return render(request,'myApp/sharebymail.html',d)