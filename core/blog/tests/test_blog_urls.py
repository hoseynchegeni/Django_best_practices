from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from ..views import indexView, PostDetailView, PostList
# Create your tests here.
class TestUrl(TestCase):
    def test_blog_index_url_resolve(self):
        url = reverse('blog:ClassBasedView')
        self.assertEqual(resolve(url).func.view_class,indexView )


    def test_blog_list_url_resolve(self):
        url = reverse('blog:PostList')
        self.assertEqual(resolve(url).func.view_class,PostList )


    def test_blog_detail_url_resolve(self):
        url = reverse('blog:PostDetail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class,PostDetailView )