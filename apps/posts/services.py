import requests
from .models import Post
API_URL = "https://jsonplaceholder.typicode.com/posts"

# GET ALL POST FROM API JSON PLACEHOLDER
def get_all_post_from_api():
    post_count = Post.objects.all().count() 
    if post_count > 0:
        return None       
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    