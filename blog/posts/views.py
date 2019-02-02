# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from .models import Post
from django.views.generic import ListView

from .forms import PostForm


class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'


class PostCategoryLiew(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        print(self.kwargs)
        return self.model.objects.filter(category__id=category_id)


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
            post = Post(title=form.cleaned_data['title'],
                        content=form.cleaned_data['content'],
                        category=form.cleaned_data['category']
                        )
            post.save()
            print('from here')
            return HttpResponseRedirect('/posts')
        else:
            # return redirect()
            return render(request, 'posts/add_post.html', {'form': form})

    elif request.method == 'GET':
        form = PostForm()

    return render(request, 'posts/add_post.html', {'form': form})


