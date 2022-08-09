from django.db import models

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)


#1대1관계 게시물-댓글 모델

class Review(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
