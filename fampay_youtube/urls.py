"""fampay_youtube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from youtube_api.views import videoDataView,videoDataSearchView

urlpatterns = [
    path('admin/', admin.site.urls),

    ## API endpoints
    path('',videoDataView.as_view(),name='video-data-view'),
    path('searchVideo/', videoDataSearchView.as_view(),name='video-data-search-view')
]
