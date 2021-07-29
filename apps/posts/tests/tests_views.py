from rest_framework import status

from apps.posts.tests.test_setup import TestSetup

class TestPostsViews(TestSetup):

    def test_get_all_posts(self):
        response = self.client.get(self.all_posts_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),100)
    
    def test_detail_post(self):
        title = "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
        id = 1
        userId = 1
        response = self.client.get(self.detail_post_url)        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('id'), id)
        self.assertEqual(response.data.get('userId'), userId)
        self.assertEqual(response.data.get('title'), title)


    def tests_detail_post_not_found(self):
        response = self.client.get(self.detail_notFound_post_url)        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_update_post(self):
        new_title = "testssunt aut facere repellat provident occaecati excepturi optio reprehenderit"
        new_body = "testbodyssunt aut facere repellat provident occaecati excepturi optio reprehenderit"
        data = {
            'id': 1,
            'userId': 1,
            'title': new_title,
            'body': new_body
        }
        response = self.client.put(self.detail_post_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('title'), new_title)
        self.assertEqual(response.data.get('body'), new_body)
        self.assertEqual(response.data.get('id'), 1)
        self.assertEqual(response.data.get('userId'), 1)
    
    def test_delete_post(self):
        response = self.client.delete(self.detail_post_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)










