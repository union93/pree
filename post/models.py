from datetime import timezone

from django.conf import settings
from django.contrib.auth import get_user_model
from accounts.models import User
from django.db import models
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    title = models.TextField(verbose_name='제목', max_length=50)
    text = models.TextField(verbose_name='내용')
    image = models.ImageField(upload_to= 'timeline_post/%Y/%m/%d')
    #created_date = models.DateField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "text : " +self.title
    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('post:detail', args=[self.id])

    def get_image_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.image)



