from django.db import models

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)


#1대1관계 게시물-댓글 모델

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=200)
    movie = models.ForeignKey(Movie, null=False,default='',on_delete=models.CASCADE)



# Create your models here.
