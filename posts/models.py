from django.db import models

# Create your models here.


#This model represents the structure of the table that will store the posts
class Post(models.Model):
    userId = models.BigIntegerField()
    title = models.CharField(max_length=200)
    body = models.TextField()
