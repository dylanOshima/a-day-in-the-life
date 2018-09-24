from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Video, Page
from .search import youtube_search

def home (request):
    return render(request, 'videos/home.html')

def page (request, page_number=""):
    Video.objects.all().delete()
    Page.objects.all().delete()
    v_list, t1, t2 = youtube_search(page_number)

    for vid,thu,c in v_list:
        v=Video(title=vid, thumbnail=thu, code=c)
        v.save()
        
    tok1=Page(number=t1) 
    
    tok1.save()   
    if (t2):
       tok2=Page(number=t2)
       tok2.save()
       videos_list=Video.objects.all()
       context = {
        'videos_list': videos_list,
        'page1': tok1,
        'page2': tok2
        }
    else: 
      videos_list=Video.objects.all()
      context = {
        'videos_list': videos_list,
        'page1': tok1,
        
        }
    return render(request, 'videos/index.html', context)



def detail(request, video_id):
    return HttpResponse("Fuck you, this is video number %s" % video_id)
    
