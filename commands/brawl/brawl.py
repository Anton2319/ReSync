# CatOS-type package
author = 'aGrIk'
mode = 'start'
deps = 'None'
identificator = 'brawl'
command_ru = 'бравл'
description = 'Статистика игрока Brawl Stars по тэгу'

if not parameter.startswith("#"): parameter = "%23" + parameter
parameter = parameter.replace("#", "%23")

req = requests.get("https://api.brawlstars.com/v1/players/" + parameter, headers={"authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjE2MWJiZGM0LTkzN2MtNGRmOC1iYjg2LTg3YTY2NTRiYmYxNyIsImlhdCI6MTYyNDk5MTI4Nywic3ViIjoiZGV2ZWxvcGVyL2QxZDMyYjAyLTg2ZTItYThmNC1mYWFiLTk2MTM2NzJkYjhhYiIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTc2LjU3LjIyMC4xMDEiXSwidHlwZSI6ImNsaWVudCJ9XX0.1h8KF8G4bvuCz85x7fdrFbXs0SfifOgsFBSOn7wBe8Zh1l7cRcRXpfdIAC2Vle-14XX0enXehNwTrsZNssA3nA"})

if req.status_code == 200:
    reqjs = req.json()
    message(f"""
Информация об игроке:

Ник: {reqjs["name"]}
Тег: {reqjs["tag"]}
Уровень: {reqjs["expLevel"]}
Трофеев: {reqjs["trophies"]}
Максимум трофеев: {reqjs["highestTrophies"]}

Побед 3 на 3: {reqjs["3vs3Victories"]}
Побед 2 на 2: {reqjs["duoVictories"]}
Одиночных побед: {reqjs["soloVictories"]}

""", reply=True)
elif req.status_code == 503:
    message("На сервере Brawl Stars временно проводятся технические работы, информация недоступна.", reply=True)
elif req.status_code == 429:
    message("Ошибка на стороне сервера Brawl Stars, информация недоступна.", reply=True)
    mta("Команда \"бравл\": превышен лимит запросов по токену API (429 HTTP). Информация от сервера: " + req.text)
elif req.status_code == 403:
    message("Ошибка на стороне сервера Brawl Stars, информация недоступна.", reply=True)
    mta("Команда \"бравл\": токен потерял доступ к API (403 HTTP). Информация от сервера: " + req.text)
else:
    message("Информация об игроке не найдена. Проверьте, верно ли вы ввели тег игрока.", reply=True)