from django.shortcuts import render

# rest_framework
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.http import JsonResponse

from .serializers import videoDataSerializer
from .models import videoData

class videoDataView(mixins.ListModelMixin,
    generics.GenericAPIView,
    mixins.CreateModelMixin):

    serializer_class = videoDataSerializer
    queryset = videoData.objects.all().order_by('-pub_date_time')

    def get(self, reqeust, *args, **kwargs):
        return self.list(reqeust, *args, **kwargs)
    
    # def post(self, reqeust, *args, **kwargs):
    #     return self.create(reqeust, *args, **kwargs)