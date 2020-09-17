from datetime import datetime
from django.db import models

# Create your models here.


class VideoData(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    title = models.CharField(max_length=254)
    description = models.CharField(max_length=254, blank=True)
    publishing_datetime = models.DateTimeField(blank=True, default=datetime.now)
    thumbnails_urls = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.id, self.title[:10])

    class Meta:
        app_label = 'youtube'
