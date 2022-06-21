from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    # title
    title = models.CharField(max_length=128)
    # text
    text = models.TextField(blank=True)
    # author
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # created_datetime
    created_datetime = models.DateTimeField(auto_now_add=True)
    # modified_datetime
    modified_datetime = models.DateTimeField(auto_now=True)
    # publish_datetime
    publish_datetime = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title