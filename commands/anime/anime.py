# CatOS-type package
author = "Anton2319"
mode = "pic"
deps = 'None'
command_ru = 'аниме'
description = 'RE-anime'

print("Animee!!")
req = requests.post("https://api.deepai.org/api/toonify", data={"image": get(ReadFF("argv_picture.txt")).content}, headers={'api-key': 'b99bb476-5feb-4979-92ef-e66ff06546aa'})
print(req)
message(req.json())