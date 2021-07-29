from django.db import models

# Create your models here.


#This model represents the structure of the table that will store the posts
class Post(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userId = models.BigIntegerField()
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return f"{self.id} - {self.title} - {self.userId}"