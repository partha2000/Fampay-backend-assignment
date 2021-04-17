from django.db import models

# Create your models here.
class videoData(models.Model):
    title = models.CharField(max_length= 50)
    description = models.TextField()
    channel_name = models.CharField(max_length= 20)
    pub_date_time = models.DateTimeField()
    thumbnailURL = models.URLField()

class testModel(models.Model):
    name = models.CharField(max_length= 10)
    