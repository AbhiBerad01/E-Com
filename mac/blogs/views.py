from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost


def index(request):
    posts = Blogpost.objects.all()
    params = {'posts': posts}
    return render(request, 'blogs/index.html', params)


def blogPost(request, post_id):
    post = Blogpost.objects.filter(post_id=post_id)[0]
    print(post)
    return render(request, 'blogs/blogpost.html',{'post' : post})
