from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request, 'posts/post_list.html', context=context)

def post_detail(request,post_id):
    post = Post.objects.get(pk = post_id)
    context = {'post' : post}
    return render(request, 'posts/post_detail.html', context=context)

def index(request):
    #body
    return HttpResponse("welcome to my weblog")

def home(request):
    return HttpResponse("<h3> here is what i want to share<h3>")
