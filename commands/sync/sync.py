import math
from pprint import pprint

import numpy
import requests

from configs.tokens import youtubeDataApi_token

global playlistID
playlistID = parameter

def pageProcess(pageToken):
    global playlistID
    payload = {"key": youtubeDataApi_token, "maxResults": "5", "playlistId": playlistID, "part": "contentDetails", "pageToken": pageToken}
    headers = {'content-type': 'application/json'}
    r = requests.get('https://youtube.googleapis.com/youtube/v3/playlistItems', params=payload, headers=headers)
    json_data = r.json()
    for video in json_data["items"]:
        os.system('yt-dlp -f bestvideo+bestaudio --merge-output-format mp4 https://youtube.com/watch?v=' +
                  video["contentDetails"]["videoId"] + ' --output download.mp4')
        os.system('telegram-send --video download.mp4 --caption https://youtube.com/watch?v=' + video["contentDetails"][
            "videoId"])
        os.system('rm download.mp4')

pageToken = ""
payload = {"key": youtubeDataApi_token, "maxResults": "5", "playlistId": playlistID, "part": "contentDetails"}
headers = {'content-type': 'application/json'}
r = requests.get('https://youtube.googleapis.com/youtube/v3/playlistItems', params=payload, headers=headers)
json_data = r.json()
payload = {"key": youtubeDataApi_token, "maxResults": "5", "playlistId": playlistID, "part": "contentDetails", "pageToken": json_data["nextPageToken"]}
r = requests.get('https://youtube.googleapis.com/youtube/v3/playlistItems', params=payload, headers=headers)
json_data = r.json()
pageToken = json_data["prevPageToken"]
i = 0

while math.ceil((json_data["pageInfo"]["totalResults"] / json_data["pageInfo"]["resultsPerPage"])) > i:
    pageProcess(pageToken)
    payload = {"key": youtubeDataApi_token, "maxResults": "5", "playlistId": playlistID, "part": "contentDetails", "pageToken": pageToken}
    r = requests.get('https://youtube.googleapis.com/youtube/v3/playlistItems', params=payload, headers=headers, )
    json_data = r.json()
    try:
        json_data["nextPageToken"]
    except:
        break
    if json_data["nextPageToken"]:
        pageToken = json_data["nextPageToken"]
    i = i+1

print("done")
message("Синхронизация завершена!")