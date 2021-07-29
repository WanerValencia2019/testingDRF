from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer
from .services import get_all_post_from_api


"""class SavePostFromAPI(APIView):
    model = Post
    serializer_class = PostSerializer

    def get_queryset(self):
        data = get_all_post_from_api()
        return data
    
    def get(self, request, *args, **kwargs):
        query = self.get_queryset()

        return Response("Datos obtenidos", )"""
    

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()    
    serializer_class = PostSerializer

    def initial(self, request, *args, **kwargs):
        api_response = get_all_post_from_api()
        print(api_response)
        return super().initial( request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return Response("Todo perfecto",status.HTTP_200_OK)