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
        if api_response is not None and self.get_queryset().count() == 0: 
            serialized  =  PostSerializer(data=api_response, many=True)
            serialized.is_valid(raise_exception=True)
            serialized.save()
        return super().initial( request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        posts = self.get_serializer(queryset, many=True)
        data = posts.data
        return Response(data,status.HTTP_200_OK)

