# CatOS-type package
author = "catwared"
mode = "start"
deps = 'None'
identificator = 'screenshot'
command_ru = 'скрин'
description = 'Скриншотит сайт при помощи roughs.ru'

message("Дёргаю roughs.ru...")
picture(f"https://roughs.ru/api/screenshot?url={parameter}&source_from=vk.com/catpy", "Ваш скриншот: ")
