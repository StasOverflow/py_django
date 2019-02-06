from django.test import TestCase
from .models import Category, Post
from django.urls import reverse


# Create your tests here.
class PostTestCase(TestCase):

    category_name = 'test_category'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(name=cls.category_name, is_active=True)
        # has a lifetime of this method's classes
        # has an opposite method tearDownClass
        pass

    def setUp(self):
        # has a lifetime of a single test time
        # has an opposite method tearDown
        pass

    def test_post_list(self):
        p = Post.objects.create(title='SuperTitle',
                                content='friugvfndngp;dfhgfhbgfbhgyyy5666666', category=self.category)
        postlisturl = 'posts/index'
        r = self.client.get(postlisturl)
        self.assertEquals(r.context['posts'], 2)
        self.assertEquals(r.status_code, 200)

    def test_pos_add(self):
        post_params = {'title': 'SuperTitle2',
                       'content': 'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh',
                       'category': self.category}
        count_post = Post.objects.count()  # get number of posts from db
        r = self.client.post('posts/index', post_params)
        if r.status_code == 200:
            self.assertEquals(Post.objects.count() + 1, count_post)
