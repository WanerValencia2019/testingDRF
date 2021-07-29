from apps.posts.tests.test_setup import TestSetup
from django.urls import resolve
from apps.posts.views import PostViewSet

class TestPostsUrls(TestSetup):
    def test_url_list_post(self):
        url_resolved = resolve(self.all_posts_url)
        self.assertEqual(url_resolved.func.cls, PostViewSet)
        self.assertEqual(url_resolved.url_name, self.post_all_url_name)

    def test_url_detail_post(self):
        url_resolved = resolve(self.detail_post_url)
        self.assertEqual(url_resolved.func.cls, PostViewSet)
        self.assertEqual(url_resolved.url_name, self.post_detail_url_name)
        self.assertEqual(len(url_resolved.kwargs), 1)
        
