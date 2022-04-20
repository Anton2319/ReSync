import math
from pprint import pprint

import numpy
import requests

from configs.tokens import youtubeDataApi_token

global playlistID
playlistID = parameter
global uploaded_content
uploaded_content = []
for x in ReadFF("usr/syncronized.txt").split("\n"):
    uploaded_content.append(x)

def pageProcess(pageToken):
    global playlistID
    global uploaded_content
    if pageToken is None:
        payload = {"key": youtubeDataApi_token, "maxResults": "5", "playlistId": playlistID, "part": "contentDetails"}
    else:
        payload = {"key": youtubeDataApi_token, "maxResults": "5", "playlistId": playlistID, "part": "contentDetails",
                   "pageToken": pageToken}
    headers = {'content-type': 'application/json'}
    r = requests.get('https://youtube.googleapis.com/youtube/v3/playlistItems', params=payload, headers=headers)
    json_data = r.json()
    for video in json_data["items"]:
        if 'https://youtube.com/watch?v='+video["contentDetails"]["videoId"] not in uploaded_content:
            os.system('yt-dlp -f bestvideo+bestaudio --merge-output-format mp4 https://youtube.com/watch?v=' +
                      video["contentDetails"]["videoId"] + ' --output download.mp4')
            os.system('telegram-send --video download.mp4 --caption https://youtube.com/watch?v=' + video["contentDetails"][
                "videoId"])
            os.system('rm download.mp4')
            PlusWrite('https://youtube.com/watch?v='+video["contentDetails"]["videoId"]+'\n', "usr/syncronized.txt")

pageToken = ""
payload = {"key": youtubeDataApi_token, "maxResults": "5", "playlistId": playlistID, "part": "contentDetails"}
headers = {'content-type': 'application/json'}
r = requests.get('https://youtube.googleapis.com/youtube/v3/playlistItems', params=payload, headers=headers)
json_data = r.json()
payload = {}
try:
    payload = {"key": youtubeDataApi_token, "maxResults": "5", "playlistId": playlistID, "part": "contentDetails", "pageToken": json_data["nextPageToken"]}
except:
    payload = {"key": youtubeDataApi_token, "maxResults": "5", "playlistId": playlistID, "part": "contentDetails"}

r = requests.get('https://youtube.googleapis.com/youtube/v3/playlistItems', params=payload, headers=headers)
json_data = r.json()
try:
    pageToken = json_data["prevPageToken"]
except:
    pageToken = None
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
    try:
        if json_data["nextPageToken"]:
            pageToken = json_data["nextPageToken"]

    except:
        break
    i = i+1

print("done")
message("Синхронизация завершена!")