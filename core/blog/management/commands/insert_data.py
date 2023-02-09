from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import User, Profile
from blog.models import Post, Category
from random import choice
from datetime import datetime

category_list = [
    'It',
    'Design',
    'Meme'
]

class Command(BaseCommand):
    help = 'Inserting dummy data'
    def __init__(self,*args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **kwargs):
        for i in category_list:
            Category.objects.get_or_create(name = i)

        for _ in range(10):
            user = User.objects.create_user(email = self.fake.email(), password= "test@123456")
            profile = Profile.objects.get(user = user)
            profile.first_name = self.fake.first_name()
            profile.last_name = self.fake.last_name()
            profile.desc = self.fake.paragraph(nb_sentences = 5)
            profile.save()
            Post.objects.create(
                author = profile,
                title = self.fake.paragraph(nb_sentences = 1),
                content = self.fake.paragraph(nb_sentences = 10),
                status = choice([True, False]),
                category = Category.objects.get(name = choice(category_list)),
                published_date = datetime.now()
            )