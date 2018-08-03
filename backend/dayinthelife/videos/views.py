from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Video
from .search import youtube_search

def index (request):
    videos_list = youtube_search()
    for video in videos_list:
        v=Video(title=video)
        v.save()
    context = {
        'videos_list': videos_list,
        }
    return render(request, 'videos/index.html', context)

def detail(request, video_id):
    return HttpResponse("Fuck you, this is video number %s" % video_id)
    
