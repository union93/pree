from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Community(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='community_user')
    title = models.TextField(verbose_name='제목', max_length=50)
    text = models.TextField(verbose_name='내용')
    image = models.ImageField(upload_to= 'timeline_community/%Y/%m/%d')
    created = models.DateField(auto_now_add=True) #post는 DateTimeField
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return "text : " +self.title
    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
       return reverse('community:detail', args=[self.id])
