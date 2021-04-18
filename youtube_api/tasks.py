from celery import shared_task
from googleapiclient.discovery import build
import json
from .models import videoData
from django.utils import dateparse

## Background task to periodically fetch youtube video data
@shared_task
def periodic_task():
    print("Youtube data is being fetched")

    ## Keep the API key secret in production 
    api_key = 'AIzaSyBR19SQAg3n1kKJzI6Gv37PYFmrDoMPR-w'
    youtube_service = build('youtube', 'v3',developerKey=api_key)

    search_videos = youtube_service.search().list(
            part="snippet",
            maxResults=50,
            order="date",
            publishedAfter="2021-04-10T00:00:00Z",
            type="video",
            q="valorant"
    )
    try:
        response = search_videos.execute()  
    except:
        response = None
        print("Service unavailable at the moment or the API quota has been exhausted")

    if response != None:
        for i in response['items']:
            p = videoData(
                            videoID = i['id']['videoId'],
                            title=i['snippet']['title'],
                            description=i['snippet']['description'],
                            channel_name=i['snippet']['channelTitle'],
                            pub_date_time=dateparse.parse_datetime(i['snippet']['publishedAt']),
                            thumbnailURL=i['snippet']['thumbnails']['default']['url'])
            p.save()
        print("Youtube data saved to database")

        for row in videoData.objects.all().reverse():
            if videoData.objects.filter(videoID=row.videoID).count() > 1:
                row.delete()
        print("Removed duplicate entries")
        
    youtube_service.close()