from django.db import models

# Create your models here.

from django.contrib.auth.models import User

from django.utils import timezone

from taggit.managers import TaggableManager





class Question(models.Model):
    Author = models.ForeignKey(User, related_name='question_author', on_delete=models.CASCADE)
    question = models.CharField(max_length=2000)
    content =  models.TextField(max_length=1000)
    tags = TaggableManager()
    created_at = models.DateTimeField(default=timezone.now)




  




class Answer (models.Model):
    author =  models.ForeignKey(User,related_name='answer_author',on_delete=models.CASCADE)
    answer = models.ForeignKey(Question,related_name='Answer_question',on_delete=models.CASCADE)
    question =models.CharField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
