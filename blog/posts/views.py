# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Post

from .forms import PostForm


def index(request):
    return render(request, 'posts/index.html', context={"posts": Post.objects.all()})
    # print(request.GET.dict()['group_name'])
    # return HttpResponse(str(request.GET.dict()))


def post_profile(request, post_id):
    print(post_id)
    post = Post.objects.filter(id=post_id).first()
    print(post)
    return render(request, 'posts/post_profile.html', context={"post": post})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(form.cleaned_data)
            # return HttpResponseRedirect('/thanks/')

    elif request.method == 'GET':
        form = PostForm()

    return render(request, 'posts/add_post.html', {'form': form})


