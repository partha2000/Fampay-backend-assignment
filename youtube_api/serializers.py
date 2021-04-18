from rest_framework import serializers

from .models import videoData


## Serializer class for the video data response
class videoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = videoData
        fields = (
            'videoID',
            'title',
            'description',
            'channel_name',
            'pub_date_time',
            'thumbnailURL'
        )