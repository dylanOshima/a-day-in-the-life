

import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


DEVELOPER_KEY = "AIzaSyDlYJ7cXjWyKs5R3HLSLol8ISvZ3y3olZ8"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(): 
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    
    
    search_response = youtube.search().list(
        q="a day in the life",
        part="id, snippet",
        maxResults=50).execute()
        
    videos = []
    channels = []
    
    
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                       search_result["id"]["videoId"]))
        elif search_result["id"]["kind"] == "youtube#channel":
            channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                       search_result["id"]["channelId"]))
        
    
    
    print ("Videos:\n", "\n".join(videos), "\n")
    print ("Channels:\n", "\n".join(channels), "\n")
    return videos
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", help="Search term", default="Google")
    parser.add_argument("--max-results", help="Max results", default=25)
    args = parser.parse_args()
    
    try:
        youtube_search(args)
    except (HttpError):
        print("An HTTP error occured ")
    