from django.db import models
from django.utils.timezone import now

# Create your models here.
class videoData(models.Model):
    # datetimestamp = models.DateTimeField(auto_now_add=True,editable=False)
    videoID = models.CharField(max_length=50,primary_key=True,default=1,editable=False)
    title = models.CharField(max_length= 50)
    description = models.TextField()
    channel_name = models.CharField(max_length= 20)
    pub_date_time = models.DateTimeField()
    thumbnailURL = models.URLField()

class testModel(models.Model):
    name = models.CharField(max_length= 10)
    