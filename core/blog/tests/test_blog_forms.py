from django.test import SimpleTestCase, TestCase
from ..forms import PostFrom
from .. models import Category
from datetime import datetime


class TestPostForm(TestCase):
    def test_post_form_with_valid_data(self):
        category_obj =Category.objects.create(name = 'hello')
        form = PostFrom(data = {
            'title':'test',
            'content':'this is test',
            'status':True,
            'category': category_obj,
            'published_date':datetime.now(),
        })
        self.assertTrue(form.is_valid())


    def test_post_form_with_no_data(self):
        form = PostFrom(data = {})
        self.assertFalse(form.is_valid())


