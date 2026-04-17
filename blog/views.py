from django.shortcuts import render,redirect
from .models import Post
from .forms import *
from django.db.models import Q


# from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def post_list(request):
    posts=Post.objects.filter(status='pub').order_by("date_modified")
    form_search=SearchForm()
    if 'search' in request.GET:
        form_search=SearchForm(request.GET)
        if form_search.is_valid():
            s=form_search.cleaned_data['search']
            posts=posts.filter(Q(title__contains=s)|Q(text__contains=s))
    return render(request,'blog/home.html',{'posts':posts,'form_search':form_search})

def detail(request,post_id):
    try:
        posts=Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        posts=None
    return render(request,'blog/detail.html',{'posts':posts})


    
def create(request):
    if request.method == 'POST':
       forms=New_Post(request.POST)
       if forms.is_valid():
           forms.save()
           return redirect('home')
      
    else:
        forms=New_Post()
        
    return render(request,'blog/addpost.html',{'forms':forms})



def edit(request,post_id):
    try:
        posts=Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        posts=None
    forms=New_Post(request.POST or None,instance=posts)
    if forms.is_valid():
        forms.save()
        return redirect('home')
        
    return render(request,'blog/addpost.html',{'forms':forms})

def delete (request,post_id):
    try:
        posts=Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        posts=None
    posts.delete()
    return redirect('home')