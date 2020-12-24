from django.shortcuts import render,get_object_or_404
from myApp.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
def post_list_view(request):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    d={'post_list':post_list}
    return render(request,'myApp/post_list.html',d)

def post_detail_view(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,publish__year=year,publish__month=month,publish__day=day)
    d={'post':post}
    return render(request,'myApp/post_detail.html',d)
