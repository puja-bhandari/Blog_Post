
from datetime import datetime
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=800)
    image = models.ImageField()
    

    def __str__(self):
        return self.title
    



