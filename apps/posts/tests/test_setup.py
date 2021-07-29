from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetup(APITestCase):
    def setUp(self):        
        self.all_posts_url = reverse("posts:posts-list")
        self.detail_post_url = reverse("posts:posts-detail", args=[1])
        self.detail_notFound_post_url = reverse("posts:posts-detail", args=[200])
        