from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    title = models.TextField(verbose_name='TITLE', max_length=50)
    text = models.TextField(verbose_name='TEXT')
    image = models.ImageField(upload_to= 'timeline_post/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "text : " +self.title
    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('post:detail', args=[self.id])