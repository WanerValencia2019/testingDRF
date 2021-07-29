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
    

#MODEL VIEWSET Provides each of the http methods that we can implement in a rest api quickly 
#through a model
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()    
    serializer_class = PostSerializer

    #This method will be executed every time a request is made
    def initial(self, request, *args, **kwargs):
        #Execute the function that will bring us the information from the api        
        api_response = get_all_post_from_api() #This code snippet has delays due to the amount of information we bring from the API
        #Evaluate if our posts table has information and also if the api returned data 
        if api_response is not None and self.get_queryset().count() == 0:
            #Pass the information to our serializers and store the information in our database 
            serialized  =  PostSerializer(data=api_response, many=True)
            #Validate data
            serialized.is_valid(raise_exception=True)
            #SAVE DATA
            serialized.save()
        return super().initial( request, *args, **kwargs)


