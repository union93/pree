from django.conf import settings
from django.db import models


def get_image_url(self):
    return '%s%s' % (settings.MEDIA_URL, self.image)
# Create your models here.
