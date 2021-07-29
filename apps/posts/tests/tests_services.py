from rest_framework.test import APITestCase
from apps.posts.services import get_all_post_from_api



class TestPostsServices(APITestCase):

    def test_func_get_posts_from_api(self):
        response_json = get_all_post_from_api()
        self.assertIsNotNone(response_json)
        post = response_json[0]
        self.assertTrue(post.get('id'))
        self.assertTrue(post.get('userId'))
        self.assertTrue(post.get('title'))
        self.assertTrue(post.get('body'))

