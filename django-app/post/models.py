
from django.contrib.auth.models import User
from django.db import models



class Post(models.Model):
    author = models.ForeignKey(User)
    comment = models.TextField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

