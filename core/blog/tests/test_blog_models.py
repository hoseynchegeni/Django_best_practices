from django.test import TestCase
from ..models import Post, Category
from datetime import datetime
from accounts.models import User, Profile


class TestPostModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@test.com", password="h@seyn4651"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="test",
            last_name="test",
            desc="this is test",
        )

    def test_create_post_with_valid_data(self):
        post = Post.objects.create(
            author=self.profile,
            title="test",
            content="this is test",
            status=True,
            category=None,
            published_date=datetime.now(),
        )
        self.assertEqual(post.title, "test")
