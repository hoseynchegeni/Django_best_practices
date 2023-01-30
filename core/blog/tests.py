from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import indexView
# Create your tests here.
class TestUrl(SimpleTestCase):
    def test_blog_index_url_resolve(self):
        url = reverse('blog:ClassBasedView')
        self.assertEqual(resolve(url).func.view_class,indexView )