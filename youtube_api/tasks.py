from celery import shared_task
from googleapiclient.discovery import build
import json
from .models import videoData
from django.utils import dateparse

@shared_task
def add(x,y):
    return x + y

@shared_task
def periodic_task():
    print("Youtube data is being fetched")
    api_key = 'AIzaSyBR19SQAg3n1kKJzI6Gv37PYFmrDoMPR-w'
    youtube_service = build('youtube', 'v3',developerKey=api_key)

    request = youtube_service.channels().list(
        part = 'statistics',
        forUsername = 'sentdex'
    )

    search_videos = youtube_service.search().list(
            part="snippet",
            maxResults=15,
            order="date",
            publishedAfter="2021-04-10T00:00:00Z",
            type="video",
            q="valorant"
    )

    response = search_videos.execute()  ## Dictionary of data
    # json_data = json.dumps(response,ensure_ascii=False ,indent=4)
    # with open('response.txt', 'w') as f:
    #     f.write(json_data)
    # print(response)

    
    # videoData.objects.all().delete()
    # print('deleted previous entries')

    for i in response['items']:
        p = videoData(videoID = i['id']['videoId'],
                        title=i['snippet']['title'],
                        description=i['snippet']['description'],
                        channel_name=i['snippet']['channelTitle'],
                        pub_date_time=dateparse.parse_datetime(i['snippet']['publishedAt']),
                        thumbnailURL=i['snippet']['thumbnails']['default']['url'])
        p.save()

        # print(i['snippet']['title'])
        # print(i['snippet']['description'])
        # print(i['snippet']['publishedAt'])
        # print(i['snippet']['thumbnails']['default']['url'])
        # print("\n")
    print("Youtube data saved to database")

    for row in videoData.objects.all().reverse():
        if videoData.objects.filter(videoID==row.videoID).count() > 1:
            row.delete()
    print("Removed duplicate entries")
    youtube_service.close()











# --------------------------------------------------------------------------------------------
# from googleapiclient.discovery import build
# import json

# api_key = 'AIzaSyBR19SQAg3n1kKJzI6Gv37PYFmrDoMPR-w'
# youtube_service = build('youtube', 'v3',developerKey=api_key)

# request = youtube_service.channels().list(
#     part = 'statistics',
#     forUsername = 'sentdex'
# )

# search_videos = youtube_service.search().list(
#         part="snippet",
#         maxResults=25,
#         order="date",
#         publishedAfter="2021-04-10T00:00:00Z",
#         type="video",
#         q="valorant"
# )

# response = search_videos.execute()  ## Dictionary of data
# json_data = json.dumps(response,ensure_ascii=False ,indent=4)
# with open('response.txt', 'w') as f:
#     f.write(json_data)
# print(response['items'][1])
# youtube_service.close()


# with open('response.txt') as json_file:
#     data = json.load(json_file)

# for i in data['items']:
#     print(i['snippet']['title'])
#     print(i['snippet']['description'])
#     print(i['snippet']['publishedAt'])
#     print(i['snippet']['thumbnails']['default']['url'])
#     print("\n")