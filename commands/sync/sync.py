from pprint import pprint

import numpy
import requests

from configs.tokens import youtubeDataApi_token
payload = {"key": youtubeDataApi_token, "maxResults": "5", "playlistId": parameter, "part": "contentDetails"}
headers = {'content-type': 'application/json'}
r = requests.get('https://youtube.googleapis.com/youtube/v3/playlistItems', params=payload, headers=headers)
json_data = r.json()
for video in json_data["items"]:
    message("https://youtube.com/watch?v="+video["contentDetails"]["videoId"])
message("Синхронизация завершена!")