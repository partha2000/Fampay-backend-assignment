from rest_framework import serializers

from .models import videoData

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

# class videoDataSearchSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = videoData
#         fields = ('title',
#                 'description')