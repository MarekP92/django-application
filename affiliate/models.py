from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    picture = models.ImageField(upload_to='akhdnsakdn')
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
