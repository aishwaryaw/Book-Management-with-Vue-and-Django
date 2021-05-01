from django.db import models
from django.contrib.auth.models import User
from io import BytesIO
from PIL import Image
from django.core.files import File
import os
# Create your models here.


class Book(models.Model):
    user = models.ForeignKey(User, related_name="books",on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    poster_image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-added_at',)

    def __str__(self):
        return f'Book - {self.title}'

    def get_poster_image(self):
        if self.poster_image:
            return self.poster_image.url
        else:
            return ''

    

