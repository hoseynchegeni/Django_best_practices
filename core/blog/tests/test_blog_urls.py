from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from ..views import indexView, PostDetailView, PostList


# Create your tests here.
class TestUrl(SimpleTestCase):
    def test_blog_index_url_resolve(self):
        url = reverse("post:ClassBasedView")
        self.assertEqual(resolve(url).func.view_class, indexView)

    def test_blog_list_url_resolve(self):
        url = reverse("post:PostList")
        self.assertEqual(resolve(url).func.view_class, PostList)

    def test_blog_detail_url_resolve(self):
        url = reverse("post:PostDetail", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, PostDetailView)
