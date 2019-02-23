# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from .models import Post
from django.views.generic import ListView
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import Http404
import time
from django.views.decorators.cache import cache_page
from django.utils.translation import gettext_lazy as _


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
        print(self.kwargs['category_id'])
        category_id = self.kwargs['category_id']
        time.sleep(5)
        return self.model.objects.filter(category__id=category_id)


@cache_page(timeout=3600)
def index(request):
    time.sleep(2)
    return render(request, 'posts/index.html', context={"posts": Post.objects.select_related('category').all()})
    # print(request.GET.dict()['group_name'])
    # return HttpResponse(str(request.GET.dict()))


def post_profile(request, post_id):
    cnt = request.session.get('cnt', 0)
    cnt += 1
    request.session['cnt'] = cnt
    print(post_id)
    post = Post.objects.filter(id=post_id).first()
    print(post)
    return render(request, 'posts/post_profile.html', context={"post": post, 'cnt': cnt})


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


def login_user(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['login'], password=request.POST['pass'])

        error_string = _("something went wrong")
        print(error_string)
        if user is None:
            raise Http404(error_string)
        login(request, user)
        return redirect('/posts/')

    return render(request, 'posts/login.html')
