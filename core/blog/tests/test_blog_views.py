from django.test import TestCase, Client
from django.urls import reverse
from ..models import Post
from accounts.models import User, Profile
from datetime import datetime



class TestBlogView(TestCase):
    def setUp(self):
        self.client = Client()


        self.user = User.objects.create_user(
            email="test@test.com", password="h@seyn4651"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="test",
            last_name="test",
            desc="this is test",
        )

        self.post = Post.objects.create(
            author=self.profile,
            title="test",
            content="this is test",
            status=True,
            category=None,
            published_date=datetime.now(),
        )

    def test_blog_index_url_successful_response(self):
        url = reverse('post:ClassBasedView')
        response = self.client.get(url)
        self.assertTrue(str(response.content).find('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='index.html')

    def test_blog_post_detail_legged_in_response(self):
        self.client.force_login(self.user)
        url = reverse('post:PostDetail', kwargs={'pk':self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_blog_post_detail_anonymous_response(self):
        url = reverse('post:PostDetail', kwargs={'pk':self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)