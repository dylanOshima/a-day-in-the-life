

import argparse

from googleapiclient.discovery import build, _findPageTokenName
from googleapiclient.errors import HttpError


DEVELOPER_KEY = "AIzaSyDlYJ7cXjWyKs5R3HLSLol8ISvZ3y3olZ8"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(pg): 
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    
    
    search_response = youtube.search().list(
        q="a day in the life",
        part="id, snippet",
        maxResults=50,
        order="viewCount",
        pageToken=pg,
        fields="prevPageToken,nextPageToken, items"
        ).execute()
        
    videos = []
    
    
    posttoken=search_response.get("nextPageToken")
    prevtoken=search_response.get("prevPageToken")
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append((search_result["snippet"]["title"], search_result["snippet"]["thumbnails"]["medium"] ["url"], search_result["id"]["videoId"]))
        
        
    
    
   
    return videos, posttoken, prevtoken
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", help="Search term", default="Google")
    parser.add_argument("--max-results", help="Max results", default=25)
    parser.add_argument("--order", help="Order", default="relevance")
    args = parser.parse_args()
    
    try:
        youtube_search(args)
    except (HttpError):
        print("An HTTP error occured ")
    