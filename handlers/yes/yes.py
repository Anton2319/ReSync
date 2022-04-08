# CatOS-type package
author = "Anton2319"
mode = "="
deps = 'None'
description = 'Пизда'

yestrue = True if re.findall(r"\b[дДdD][AАаа]+[^\wБ-Яб-яёЁ]*$\Z", text) else False
if yestrue and peer_id == -1001251682478:
    print("yestruecorrect")
    message("Пизда")
#restricted