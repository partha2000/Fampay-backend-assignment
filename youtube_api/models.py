from django.db import models

# Create your models here.
class videoData(models.Model):
    title = models.CharField()
    description = models.TextField()
    pub_date_time = models.DateTimeField()
    thumbnailURL = models.URLField()