from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import *
# Create your views here.


def index(request):
    # collect all model fileds
    articles = ExtraBlogHome.objects.all()


    return render(request, 'index.html', {'articles':articles})


def about(request):
    return render(request, 'about.html')



def home(request):
    return redirect('/home')


def post(request):
    posts =  SinglePost.objects.all()
    categories = CategoriesFiled.objects.all()
    videos = VideoPost.objects.all()
    # related = RealatedPost.objects.all()


    return render(request,'post.html', {'posts':posts,'categories':categories,'videos':videos})




def contact(request):
    return render(request,'contact.html')