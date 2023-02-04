import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime 
from accounts.models import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email='admin@admin.com',
        password = 'h@seyn4651',
        is_verified = True
        )
    return user
    


@pytest.mark.django_db
class TestPostAPi():
    def test_get_post_response_200(self, api_client, common_user):
        url = reverse('post:api_v1:post-list')
        api_client.force_login(user = common_user)
        response = api_client.get(url)
        assert response.status_code == 200


    def test_get_category_response_201(self, api_client, common_user):
        url = reverse('post:api_v1:category-list')
        data = {'name':'culture'}
        api_client.force_login(user = common_user)
        response = api_client.post(url, data)
        assert response.status_code == 201
    