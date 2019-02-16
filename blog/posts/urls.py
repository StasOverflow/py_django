from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.post_profile, name='post'),
    path('add_post/', views.add_post, name='add_post'),
    path('cbv/posts/', views.PostListView.as_view(), name='posts_list'),
    path('login/', views.login_user, name='login'),
    path('category/<int:category_id>/', cache_page(100)(views.PostCategoryLiew.as_view()), name='category_list')
]
