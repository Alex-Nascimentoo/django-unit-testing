from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

  title = models.CharField(max_length=255)
  content = models.TextField()

  likes = models.ManyToManyField(
    User,
    related_name = 'likes',
    default = None,
    blank = True
  )

  def __str__(self):
    return self.title
