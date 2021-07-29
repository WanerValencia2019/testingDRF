from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetup(APITestCase):
    #Initial config, Establish the url of our api
    def setUp(self):
        # reverse method, returns the url according to the name of our view 
        self.post_detail_url_name = "posts-detail"
        self.post_all_url_name = "posts-list"        
        self.all_posts_url = reverse("posts:posts-list")
        self.detail_post_url = reverse("posts:posts-detail", args=[1])
        self.detail_notFound_post_url = reverse("posts:posts-detail", args=[200])
        