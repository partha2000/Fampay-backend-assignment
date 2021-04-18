from django.db import models
from django.utils.timezone import now

# Model class for the video data objects
class videoData(models.Model):
    videoID = models.CharField(max_length=50,primary_key=True,editable=False)
    title = models.CharField(max_length= 50)
    description = models.TextField()
    channel_name = models.CharField(max_length= 20)
    pub_date_time = models.DateTimeField()
    thumbnailURL = models.URLField()
