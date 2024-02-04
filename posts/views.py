from typing import Any
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect , HttpResponseNotFound
from .models import Post , Comment
from .forms import PostForm
from django.views import generic

#این تابع رو کامنت کردم و قراره از شورت کات خود جنکو.ویو استفاده کنم برای  نوشتن همین تابع ولی به صورت کلاس.
def post_list(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request, 'posts/post_list.html', context=context)

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

# این تابع رو کامنت کردم و قراره از شورت کات خود جنکو.ویو استفاده کنم برای  نوشتن همین تابع ولی به صورت کلاس.
def post_detail(request,post_id):
#     try:
#         post = Post.objects.get(pk = post_id)
#     except Post.DoesNotExist:
#         return HttpResponseNotFound("post does not exist")
    post = get_object_or_404(Post , pk = post_id)
    comments = Comment.objects.filter(post=post)
    context = {'post' : post , 'comments': comments}
    return render(request, 'posts/post_detail.html', context=context)

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs):
        context =  super(PostDetail, self).get_context_data()
        context['comments'] = Comment.objects.filter(post = kwargs['object'].pk)
        return context


def index(request):
    #body
    return HttpResponse("welcome to my weblog")

def home(request):
    return HttpResponse("<h3> here is what i want to share<h3>")

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(type(form.cleaned_data))
            print(form.cleaned_data)
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts/')
    else:
        form = PostForm()
        return render(request , 'posts/post_create.html', {'form':form})
    