req = requests.post("https://api.deepai.org/api/toonify", data={"image": ReadFF("argv_picture.txt")}, headers={'api-key': 'a31ae70e-89a4-496f-86b9-7ada67f20d6c'})
message(req.json())