from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name='home'),
    path ('<int:video_id>/', views.detail, name='detail'),
    path('<str:page_number>/', views.page, name='nextpages')
    ]
