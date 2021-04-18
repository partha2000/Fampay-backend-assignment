from django.shortcuts import render

# rest_framework
from rest_framework import mixins 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.settings import api_settings
from rest_framework import filters

from .serializers import videoDataSerializer
from .models import videoData

## Simple GET API to fetch video data stored in the database in a reverse chronological order
class videoDataView(mixins.ListModelMixin,
    generics.GenericAPIView,
    mixins.CreateModelMixin):
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS ## This will auto paginate the repsonse

    serializer_class = videoDataSerializer
    queryset = videoData.objects.all().order_by('-pub_date_time')  ## Return videos in a reverse chronologial order

    def get(self, reqeust, *args, **kwargs):
        return self.list(reqeust, *args, **kwargs)

## Search API to search the stored videos using their title and description.
class videoDataSearchView(generics.ListAPIView):

    # title and description have been added to match the search querry with both of them
    search_fields = [
        'title',
        'description'
    ]

    # fields for ordering the response
    ordering_fields = [
        'pub_date_time',
        'title'] 
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter)
    queryset = videoData.objects.all().order_by('-pub_date_time')
    serializer_class = videoDataSerializer
